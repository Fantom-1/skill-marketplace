import json
import sys

def main():
    try:
        with open("prompts_parsed.json", "r") as f:
            prompts = json.load(f)
        with open("audit_progress.json", "r") as f:
            progress = json.load(f)
    except Exception as e:
        print("Error reading files:", e)
        return

    completed = progress.get("completed", {})
    
    # Find the first site that has missing gemini prompts
    missing_by_site = {}
    for p in prompts:
        agent = "gemini"
        key = f"{agent}:{p['file_key']}"
        if key not in completed:
            site_id = p['site_id']
            if site_id not in missing_by_site:
                missing_by_site[site_id] = []
            missing_by_site[site_id].append(p)
            
    if not missing_by_site:
        print("DONE")
        return
        
    next_site = list(missing_by_site.keys())[0]
    site_prompts = missing_by_site[next_site]
    
    print(f"SITE_ID:{next_site}")
    print(f"URL:{site_prompts[0]['site_url']}")
    for p in site_prompts:
        print(f"PROMPT:{p['file_key']}|{p['prompt_text']}")

if __name__ == "__main__":
    main()
