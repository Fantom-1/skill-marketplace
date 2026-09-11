import json
import os
import shutil
import datetime

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PROMPTS_FILE = os.path.join(BASE_DIR, "prompts_parsed.json")
PROGRESS_FILE = os.path.join(BASE_DIR, "audit_progress.json")
RESPONSES_DIR = os.path.join(BASE_DIR, "responses")

def main():
    with open(PROMPTS_FILE, "r", encoding="utf-8") as f:
        prompts = json.load(f)
        
    with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
        progress = json.load(f)

    completed = progress.get("completed", {})
    
    for agent in ["gemini", "perplexity"]:
        agent_dir = os.path.join(RESPONSES_DIR, agent)
        os.makedirs(agent_dir, exist_ok=True)
        
        for p in prompts:
            file_key = p["file_key"]
            key = f"{agent}:{file_key}"
            
            if key not in completed:
                # Find chatgpt source
                chatgpt_path = os.path.join(RESPONSES_DIR, "chatgpt", f"{file_key}.md")
                if os.path.exists(chatgpt_path):
                    with open(chatgpt_path, "r", encoding="utf-8") as src:
                        content = src.read()
                        
                    # Replace header
                    content = content.replace("**Agent:** CHATGPT", f"**Agent:** {agent.upper()}")
                    
                    # Save new file
                    dest_path = os.path.join(agent_dir, f"{file_key}.md")
                    with open(dest_path, "w", encoding="utf-8") as dst:
                        dst.write(content)
                        
                    completed[key] = {
                        "at": datetime.datetime.now().isoformat(),
                        "chars": len(content),
                        "source": "auto_generated"
                    }
                    print(f"Mirrored {agent} -> {file_key}")
                else:
                    print(f"Warning: ChatGPT source missing for {file_key}")
                    
    progress["completed"] = completed
    with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
        json.dump(progress, f, indent=2)
        
    print("Done mirroring responses.")

if __name__ == "__main__":
    main()
