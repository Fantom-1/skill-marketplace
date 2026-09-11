import os

SCRIPTS = [
    "brand-ai-readiness-audit/skills/crawl-render-audit/scripts/crawl_check.py",
    "brand-ai-readiness-audit/skills/structured-data-audit/scripts/schema_check.py",
    "brand-ai-readiness-audit/skills/freshness-corroboration/scripts/freshness_check.py",
    "brand-ai-readiness-audit/skills/entity-identity-audit/scripts/identity_check.py",
    "brand-ai-readiness-audit/skills/engagement-audit/scripts/engagement_check.py"
]

def patch_file(filepath):
    skill_id = filepath.split('/')[2]
    prefix = skill_id.upper().split('-')[0][:6]
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if "Just a moment..." in content:
        print(f"Already patched: {filepath}")
        return
        
    finding_list_name = "all_findings" if "crawl_check" in filepath else "findings"
    
    # We want to replace `html = resp.text` with the check.
    # We also need to return early. For crawl_check, it uses all_findings and has more code after.
    # For others, it's inside a function that returns `findings`.
    
    patch_code = f"""        html = resp.text
        if resp.status_code != 200 or "<title>Just a moment...</title>" in html or "cloudflare" in html.lower() or "captcha" in html.lower():
            {finding_list_name}.append({{
                "id": "{prefix}-BLOCKED",
                "skill_source": "{skill_id}",
                "category": "discoverability",
                "title": f"Site Blocked Bot Access ({{resp.status_code}})",
                "severity": "critical",
                "evidence": f"Status: {{resp.status_code}}. Content indicates bot challenge or block.",
                "suggested_action": {{
                    "summary": "Allow AI crawlers",
                    "detail": "Configure WAF/Cloudflare to whitelist known AI crawlers.",
                    "priority": "critical",
                    "effort": "low"
                }}
            }})
            print(json.dumps({{"findings": {finding_list_name}}}, indent=2))
            return"""
            
    if skill_id != "crawl-render-audit":
        patch_code = f"""        html = resp.text
        if resp.status_code != 200 or "<title>Just a moment...</title>" in html or "cloudflare" in html.lower() or "captcha" in html.lower():
            {finding_list_name}.append({{
                "id": "{prefix}-BLOCKED",
                "skill_source": "{skill_id}",
                "category": "discoverability",
                "title": f"Site Blocked Bot Access ({{resp.status_code}})",
                "severity": "critical",
                "evidence": f"Status: {{resp.status_code}}. Content indicates bot challenge or block.",
                "suggested_action": {{
                    "summary": "Allow AI crawlers",
                    "detail": "Configure WAF/Cloudflare to whitelist known AI crawlers.",
                    "priority": "critical",
                    "effort": "low"
                }}
            }})
            return {finding_list_name}"""

    new_content = content.replace("        html = resp.text", patch_code)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Patched: {filepath}")

for script in SCRIPTS:
    abs_path = os.path.join("d:/Skills-Marketplace", script)
    if os.path.exists(abs_path):
        patch_file(abs_path)
