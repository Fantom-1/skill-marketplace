"""
Export all 120 prompts as individual .txt files for bulk pasting.
Creates: prompts_export/<agent>/ with all prompt files ready to paste.

This is an alternative to the interactive runner — you can open each file,
copy its content, and paste into the AI web UI at your own pace.
"""

import json
import os

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PROMPTS_FILE = os.path.join(BASE_DIR, "prompts_parsed.json")
EXPORT_DIR = os.path.join(BASE_DIR, "prompts_export")


def main():
    with open(PROMPTS_FILE, "r", encoding="utf-8") as f:
        prompts = json.load(f)

    # Group prompts by site
    sites = {}
    for p in prompts:
        sid = p["site_id"]
        if sid not in sites:
            sites[sid] = []
        sites[sid].append(p)

    total = 0
    for agent in ["chatgpt", "gemini", "perplexity"]:
        agent_dir = os.path.join(EXPORT_DIR, agent)
        os.makedirs(agent_dir, exist_ok=True)

        for site_id in sorted(sites.keys()):
            site_prompts = sorted(sites[site_id], key=lambda x: x["prompt_num"])
            site_slug = site_prompts[0]["site_slug"]
            site_name = site_prompts[0]["site_name"]

            # Create a single file per site with ALL 6 prompts separated
            # This way user can paste all 6 into one chat session
            combined_path = os.path.join(agent_dir, f"site_{site_id:02d}_{site_slug}_ALL_PROMPTS.txt")
            with open(combined_path, "w", encoding="utf-8") as f:
                f.write(f"{'='*70}\n")
                f.write(f"SITE {site_id}: {site_name} | AGENT: {agent.upper()}\n")
                f.write(f"{'='*70}\n\n")
                f.write(f"NOTE: Run each prompt below SEPARATELY in {agent.upper()}.\n")
                f.write(f"Copy the AI's response for each prompt into the corresponding\n")
                f.write(f"response file in: responses/{agent}/\n\n")

                for p in site_prompts:
                    f.write(f"\n{'='*70}\n")
                    f.write(f"PROMPT {p['prompt_num']}/6: {p['prompt_label']}\n")
                    f.write(f"Save response to: responses/{agent}/{p['file_key']}.md\n")
                    f.write(f"{'='*70}\n\n")
                    f.write(p["prompt_text"])
                    f.write("\n\n")

            # Also create individual prompt files for one-at-a-time workflow
            for p in site_prompts:
                individual_path = os.path.join(agent_dir, f"{p['file_key']}.txt")
                with open(individual_path, "w", encoding="utf-8") as f:
                    f.write(p["prompt_text"])
                total += 1

    print(f"Exported {total} individual prompt files")
    print(f"Plus {len(sites) * 3} combined site files (all 6 prompts per site)")
    print(f"Output: {EXPORT_DIR}/")
    print(f"\nStructure:")
    print(f"  prompts_export/")
    for agent in ["chatgpt", "gemini", "perplexity"]:
        print(f"    {agent}/")
        print(f"      site_01_nike_ALL_PROMPTS.txt       <- all 6 prompts in one file")
        print(f"      site_01_nike_prompt_01.txt          <- individual prompt")
        print(f"      site_01_nike_prompt_02.txt")
        print(f"      ...")


if __name__ == "__main__":
    main()
