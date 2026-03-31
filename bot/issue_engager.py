import os
import json
from github import Github
from bot.ai_helper import get_ai_response

def get_tone(repo_name):
    try:
        config_path = os.path.join("config", "repo_tones.json")
        if os.path.exists(config_path):
            with open(config_path, "r", encoding="utf-8") as f:
                tones = json.load(f)
                return tones.get(repo_name, tones.get("default", "professional and helpful"))
    except:
        pass
    return "professional and helpful"

def engage_good_first_issue():
    token = os.getenv("GITHUB_TOKEN") or os.getenv("GIT_TOKEN")
    if not token:
        print("GITHUB_TOKEN or GIT_TOKEN not set. Skipping good first issues.")
        return None

    try:
        g = Github(token)
        user = g.get_user()
    except Exception as e:
        print(f"GitHub Error: {e}")
        return None
    
    # Search query
    query = "label:\"good first issue\" state:open language:python language:javascript is:issue"
    issues = g.search_issues(query, sort="created", order="desc")
    
    if issues.totalCount > 0:
        target_issue = issues[0]
        # Only comment if we haven't already
        comments = target_issue.get_comments()
        already_commented = any(c.user.login == user.login for c in comments)
        
        if not already_commented:
            prompt = f"Write a short, encouraging comment for a beginner taking on their first open source issue. The issue is titled: '{target_issue.title}'. Keep it very brief and friendly, and don't include any placeholders."
            try:
                # Use AI to generate the comment body
                comment_body = get_ai_response(prompt)
                
                # We NO LONGER post automatically.
                # Instead, we just return the draft.
                print(f"Drafted review for good-first-issue: {target_issue.title}")
                return {
                    "type": "good_first_issue",
                    "url": target_issue.html_url,
                    "title": target_issue.title,
                    "draft": comment_body
                }
            except Exception as e:
                print(f"Failed to generate draft: {e}")
        else:
            print("Already commented on the newest good-first-issue.")
    
    return None

def handle_own_repo_issues():
    github_token = os.getenv("GITHUB_TOKEN") or os.getenv("GIT_TOKEN")
    if not github_token:
        print("Missing GITHUB_TOKEN or GIT_TOKEN. Skipping own issue handler.")
        return []

    try:
        g = Github(github_token)
        user = g.get_user()
    except Exception as e:
        print(f"GitHub Error: {e}")
        return []
    
    responses = []

    # Get recent issues in owned repos
    for repo in user.get_repos(type="owner"):
        issues = repo.get_issues(state="open")
        count = 0
        for issue in issues:
            if count >= 3: # Limit to 3 for performance
                break
            count += 1
            
            if issue.comments == 0:
                print(f"Drafting response for issue {issue.title} in {repo.name}")
                
                tone = get_tone(repo.name)
                prompt = f"Write a short, {tone} open-source maintainer reply acknowledging this new issue:\nTitle: {issue.title}\nBody: {issue.body}\nDo not include any placeholders, just the comment text."
                
                try:
                    draft_reply = get_ai_response(prompt)
                    print(f"Drafted review for own issue: {issue.title}")
                    
                    responses.append({
                        "type": "own_issue",
                        "repo": repo.name,
                        "issue_title": issue.title,
                        "url": issue.html_url,
                        "draft": draft_reply
                    })
                except Exception as e:
                    print(f"Error drafting reply: {e}")
                    
    return responses
