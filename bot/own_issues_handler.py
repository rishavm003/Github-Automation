import os
from github import Github
from bot.ai_helper import get_ai_response

def handle_own_issues():
    github_token = os.getenv("GIT_TOKEN")
    if not github_token:
        print("Missing GIT_TOKEN. Skipping own issue handler.")
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
        # Use a count to limit to 5 instead of slicing to avoid PaginatedList IndexError
        count = 0
        for issue in issues:
            if count >= 5:
                break
            count += 1
            # If no comments except the creator's, or just new issue
            if issue.comments == 0:
                print(f"Drafting response for issue {issue.title} in {repo.name}")
                
                prompt = f"Write a short, friendly open-source maintainer reply acknowledging this new issue:\nTitle: {issue.title}\nBody: {issue.body}\nDo not include any placeholders, just the comment text."
                
                try:
                    draft_reply = get_ai_response(prompt)
                    # We NO LONGER post automatically.
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
