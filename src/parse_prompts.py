"""
Parse all 120 prompts from the website-audit-complete-prompts.md file.
Outputs a structured JSON file: prompts_parsed.json
"""

import re
import json
import os

MD_PATH = os.path.join(os.path.dirname(__file__), "..", "website-audit-complete-prompts.md")
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "..", "prompts_parsed.json")

# System prefix to inject into every prompt
SYSTEM_PREFIX = """IMPORTANT INSTRUCTIONS — READ BEFORE RESPONDING:
- Do NOT sugarcoat, speculate, or fill gaps with assumptions. State only raw, verifiable facts you directly extracted.
- If you visit any URL, provide the FULL URL (e.g., https://www.example.com/about) not just "the about page".
- Quote exact text from the site in quotation marks. If you cannot find something, say "NOT FOUND on site" — do not guess.
- Do NOT visit, reference, or pull information from any website other than the one specified. Zero external sources.
- Format your response with clear headings for each sub-question (a), (b), (c), etc.
- Provide raw evidence: HTML snippets, exact meta tag values, exact text passages. No paraphrasing.

---

"""

SITE_DEFINITIONS = [
    {"id": 1,  "slug": "nike",          "name": "Nike",          "url": "https://www.nike.com",           "category": "ecommerce"},
    {"id": 2,  "slug": "allbirds",      "name": "Allbirds",      "url": "https://www.allbirds.com",       "category": "ecommerce"},
    {"id": 3,  "slug": "buckmason",     "name": "Buck Mason",    "url": "https://www.buckmason.com",      "category": "ecommerce"},
    {"id": 4,  "slug": "vintageempire", "name": "Vintage Empire", "url": "https://vintageempire.shop",    "category": "ecommerce"},
    {"id": 5,  "slug": "notion",        "name": "Notion",        "url": "https://www.notion.so",          "category": "saas"},
    {"id": 6,  "slug": "asana",         "name": "Asana",         "url": "https://www.asana.com",          "category": "saas"},
    {"id": 7,  "slug": "linear",        "name": "Linear",        "url": "https://linear.app",             "category": "saas"},
    {"id": 8,  "slug": "figma",         "name": "Figma",         "url": "https://www.figma.com",          "category": "saas"},
    {"id": 9,  "slug": "viacarota",     "name": "Via Carota",    "url": "https://www.viacarota.com",      "category": "local"},
    {"id": 10, "slug": "bestlawyers",   "name": "Best Lawyers",  "url": "https://www.bestlawyers.com",    "category": "local"},
    {"id": 11, "slug": "acehotel",      "name": "Ace Hotel",     "url": "https://www.acehotel.com",       "category": "local"},
    {"id": 12, "slug": "servicemaster", "name": "ServiceMaster", "url": "https://www.servicemaster.com",  "category": "local"},
    {"id": 13, "slug": "bbc",           "name": "BBC",           "url": "https://www.bbc.com",            "category": "media"},
    {"id": 14, "slug": "lesswrong",     "name": "LessWrong",     "url": "https://www.lesswrong.com",      "category": "media"},
    {"id": 15, "slug": "outdated",      "name": "Outdated Site",  "url": "TBD",                           "category": "media"},
    {"id": 16, "slug": "techcrunch",    "name": "TechCrunch",    "url": "https://techcrunch.com",         "category": "media"},
    {"id": 17, "slug": "apple",         "name": "Apple",         "url": "https://www.apple.com",          "category": "brand"},
    {"id": 18, "slug": "zappos",        "name": "Zappos",        "url": "https://www.zappos.com",         "category": "brand"},
    {"id": 19, "slug": "buffer",        "name": "Buffer",        "url": "https://buffer.com",             "category": "brand"},
    {"id": 20, "slug": "spotify_se",    "name": "Spotify SE",    "url": "https://www.spotify.com/se-en/", "category": "brand"},
]

PROMPT_LABELS = {
    1: "Direct Brand Recall",
    2: "Factual Extraction Under Constraint",
    3: "Structured Data & Machine Readability",
    4: "Task Completion Test",
    5: "Content Depth & Freshness",
    6: "Navigation & Orientation",
}


def parse_prompts_from_md(md_path):
    """Parse the markdown file and extract prompts grouped by site and prompt number."""
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Split by site headers (## Site N:)
    site_blocks = re.split(r"(?=## Site \d+:)", content)

    all_prompts = []
    site_idx = 0

    for block in site_blocks:
        site_match = re.match(r"## Site (\d+):", block)
        if not site_match:
            continue

        site_num = int(site_match.group(1))
        if site_num < 1 or site_num > 20:
            continue

        site_def = SITE_DEFINITIONS[site_num - 1]

        # Split by prompt headers
        prompt_sections = re.split(r"### Prompt (\d+) —", block)

        for i in range(1, len(prompt_sections), 2):
            prompt_num = int(prompt_sections[i])
            prompt_body = prompt_sections[i + 1]

            # Clean up: get text until next ### or ---
            prompt_body = re.split(r"\n---\n|\n### |\n## ", prompt_body)[0]

            # Remove the label line (e.g., "Direct Brand Recall\n")
            lines = prompt_body.strip().split("\n")
            # First line is the label, skip it
            label_line = lines[0].strip()
            prompt_text = "\n".join(lines[1:]).strip()

            # Remove **Task:** prefix formatting but keep the task text
            prompt_text = re.sub(r"\*\*Task:\*\*\s*", "Task: ", prompt_text)

            all_prompts.append({
                "site_id": site_num,
                "site_slug": site_def["slug"],
                "site_name": site_def["name"],
                "site_url": site_def["url"],
                "category": site_def["category"],
                "prompt_num": prompt_num,
                "prompt_label": PROMPT_LABELS.get(prompt_num, f"Prompt {prompt_num}"),
                "prompt_text": SYSTEM_PREFIX + prompt_text,
                "file_key": f"site_{site_num:02d}_{site_def['slug']}_prompt_{prompt_num:02d}",
            })

    return all_prompts


if __name__ == "__main__":
    prompts = parse_prompts_from_md(MD_PATH)
    print(f"Parsed {len(prompts)} prompts from {len(set(p['site_id'] for p in prompts))} sites")

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(prompts, f, indent=2, ensure_ascii=False)

    print(f"Saved to {OUTPUT_PATH}")

    # Print summary
    sites_seen = set()
    for p in prompts:
        sites_seen.add(p["site_id"])
    print(f"\nSites covered: {sorted(sites_seen)}")
    print(f"Prompts per site: {len(prompts) // len(sites_seen) if sites_seen else 0}")
