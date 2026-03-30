import os
from github import Github
from bot.ai_helper import get_ai_response

def engage_good_first_issue():
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        print("GITHUB_TOKEN not set. Skipping good first issues.")
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
                
                target_issue.create_comment(f"*(Auto-drafted by AI)*\n{comment_body}")
                print(f"Commented on {target_issue.html_url}")
                return {
                    "url": target_issue.html_url,
                    "title": target_issue.title,
                    "comment": comment_body
                }
            except Exception as e:
                print(f"Failed to generate or post comment: {e}")
        else:
            print("Already commented on the newest good-first-issue.")
    
    return None
