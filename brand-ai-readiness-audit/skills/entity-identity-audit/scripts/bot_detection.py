def is_blocked_response(resp):
    if resp.status_code in (403, 429):
        return True
    
    text = resp.text.lower()
    block_markers = [
        'cloudflare', 'ray id', 'access denied', 'pardon our interruption',
        'incapsula', 'akamai', 'security check', 'please verify you are a human'
    ]
    if any(marker in text for marker in block_markers):
        return True
        
    return False
