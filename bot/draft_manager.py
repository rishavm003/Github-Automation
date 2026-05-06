import os
import json

DRAFTS_FILE = "data/drafts/pending.json"

def save_draft(type, repo, issue_url, title, draft):
    os.makedirs("data/drafts", exist_ok=True)
    
    drafts = []
    if os.path.exists(DRAFTS_FILE):
        try:
            with open(DRAFTS_FILE, "r", encoding="utf-8") as f:
                drafts = json.load(f)
        except:
            drafts = []
            
    drafts.append({
        "type": type,
        "repo": repo,
        "url": issue_url,
        "title": title,
        "draft": draft
    })
    
    with open(DRAFTS_FILE, "w", encoding="utf-8") as f:
        json.dump(drafts, f, indent=4)

def load_all_drafts():
    if not os.path.exists(DRAFTS_FILE):
        return []
    try:
        with open(DRAFTS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def clear_drafts():
    if os.path.exists(DRAFTS_FILE):
        os.remove(DRAFTS_FILE)
