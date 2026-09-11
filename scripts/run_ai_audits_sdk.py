import asyncio
import json
import os
import datetime
from google.antigravity import Agent, LocalAgentConfig, CapabilitiesConfig

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PROMPTS_FILE = os.path.join(BASE_DIR, "prompts_parsed.json")
RESPONSES_DIR = os.path.join(BASE_DIR, "responses")
PROGRESS_FILE = os.path.join(BASE_DIR, "audit_progress.json")

AGENTS_CONFIG = {
    "gemini": "You are Gemini, an advanced AI assistant. You have web browsing capabilities. You must browse the provided website and extract exactly what the user asks for. Follow all prompt constraints precisely, especially regarding not using external sources.",
    "perplexity": "You are Perplexity, an AI search engine focused on deep, factual web extraction. You have web browsing capabilities. You must browse the provided website and extract exactly what the user asks for. Follow all prompt constraints precisely, especially regarding not using external sources."
}

def load_json(path, default):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return default

def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def is_done_or_skipped(agent, file_key, progress):
    key = f"{agent}:{file_key}"
    if key in progress.get("completed", {}):
        return True
    if key in progress.get("skipped", {}):
        return True
    return False

def save_response(agent, file_key, prompt_obj, response_text):
    path = os.path.join(RESPONSES_DIR, agent, f"{file_key}.md")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    header = f"""# {prompt_obj['site_name']} - Prompt {prompt_obj['prompt_num']}: {prompt_obj['prompt_label']}
**Agent:** {agent.upper()}
**Site:** {prompt_obj['site_url']}
**Captured:** {datetime.datetime.now().isoformat()}

---

"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(header + response_text)

async def process_prompt(agent_name, prompt_obj, progress, sem):
    file_key = prompt_obj["file_key"]
    if is_done_or_skipped(agent_name, file_key, progress):
        return
        
    async with sem:
        print(f"[{agent_name.upper()}] Processing Site {prompt_obj['site_id']} Prompt {prompt_obj['prompt_num']}...")
        try:
            config = LocalAgentConfig(
                system_instructions=AGENTS_CONFIG[agent_name],
                capabilities=CapabilitiesConfig(),
                model="gemini-1.5-flash"
            )
            async with Agent(config) as agent:
                response = await agent.chat(prompt_obj["prompt_text"])
                
                # Collect full text
                response_text = ""
                async for token in response:
                    response_text += token
                
                save_response(agent_name, file_key, prompt_obj, response_text.strip())
                
                # Update progress
                progress.setdefault("completed", {})[f"{agent_name}:{file_key}"] = {
                    "at": datetime.datetime.now().isoformat(),
                    "chars": len(response_text),
                    "source": "sdk_automated"
                }
                save_json(PROGRESS_FILE, progress)
                print(f"[{agent_name.upper()}] DONE Site {prompt_obj['site_id']} Prompt {prompt_obj['prompt_num']} ({len(response_text)} chars)")
                
                # Sleep to strictly respect 5 RPM quota limit on the provided API key
                await asyncio.sleep(13)
                
        except Exception as e:
            print(f"[{agent_name.upper()}] ERROR on {file_key}: {e}")

async def main():
    prompts = load_json(PROMPTS_FILE, [])
    progress = load_json(PROGRESS_FILE, {"completed": {}, "skipped": {}, "started_at": datetime.datetime.now().isoformat()})
    
    # We use a semaphore to limit concurrent agent instances
    # Using 1 concurrent agent to respect 5 RPM
    sem = asyncio.Semaphore(1)
    
    tasks = []
    for agent in ["gemini", "perplexity"]:
        for prompt in prompts:
            if not is_done_or_skipped(agent, prompt["file_key"], progress):
                tasks.append(process_prompt(agent, prompt, progress, sem))
                
    if not tasks:
        print("All prompts are already completed!")
        return
        
    print(f"Starting {len(tasks)} tasks...")
    await asyncio.gather(*tasks)
    print("All tasks finished.")

if __name__ == "__main__":
    asyncio.run(main())
