import os
import re

SCRIPTS = [
    "brand-ai-readiness-audit/skills/crawl-render-audit/scripts/crawl_check.py",
    "brand-ai-readiness-audit/skills/structured-data-audit/scripts/schema_check.py",
    "brand-ai-readiness-audit/skills/freshness-corroboration/scripts/freshness_check.py",
    "brand-ai-readiness-audit/skills/entity-identity-audit/scripts/identity_check.py",
    "brand-ai-readiness-audit/skills/engagement-audit/scripts/engagement_check.py"
]

BOT_CHECK_LOGIC = """
        if resp.status_code != 200 or "<title>Just a moment...</title>" in html or "cloudflare" in html.lower() or "captcha" in html.lower():
            return [{
                "id": f"{skill_id.upper()[:6]}-BLOCKED",
                "skill_source": skill_id,
                "category": "discoverability",
                "title": f"Site Blocked Bot Access ({resp.status_code})",
                "severity": "critical",
                "evidence": f"Status: {resp.status_code}. Content indicates bot challenge or block.",
                "suggested_action": {
                    "summary": "Allow AI crawlers",
                    "detail": "Configure WAF/Cloudflare to whitelist known AI crawlers.",
                    "priority": "critical",
                    "effort": "low"
                }
            }]
"""

def patch_script(script_path):
    skill_id = script_path.split("/")[2]
    with open(script_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the line where resp.text is assigned
    # We will insert our check right after we get the HTML
    target_str = "html = resp.text"
    if target_str in content and "-BLOCKED" not in content:
        # Build the injected code
        injected = f"        html = resp.text\n        skill_id = '{skill_id}'" + BOT_CHECK_LOGIC.replace("\n", "\n    ", 1) # indent matching
        
        # We need to make sure we format it exactly. Let's do a simple regex replace.
        content = content.replace(target_str, f"{target_str}\n        skill_id = '{skill_id}'{BOT_CHECK_LOGIC}")
        
        # Wait, the bot check returns a finding, but in the scripts it might be expecting to extend a list.
        # Let's look at schema_check.py structure.
        pass

# Instead of regex patching, let's just write a unified fetcher or patch each manually since there are only 5. 
# Actually, the quickest way is just to manually update them via multi_replace_file_content or a custom patcher.
