import os
from github import Github

def engage_good_first_issue():
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        print("GITHUB_TOKEN not set. Skipping good first issues.")
        return None

    g = Github(token)
    
    # Search query
    query = "label:\"good first issue\" state:open language:python language:javascript"
    issues = g.search_issues(query, sort="created", order="desc")
    
    if issues.totalCount > 0:
        target_issue = issues[0]
        # Only comment if we haven't already
        user = g.get_user()
        comments = target_issue.get_comments()
        already_commented = any(c.user.login == user.login for c in comments)
        
        if not already_commented:
            comment_body = "This looks like a great first issue! I'd love to take a look at it."
            try:
                target_issue.create_comment(comment_body)
                print(f"Commented on {target_issue.html_url}")
                return {
                    "url": target_issue.html_url,
                    "title": target_issue.title,
                    "comment": comment_body
                }
            except Exception as e:
                print(f"Failed to comment: {e}")
        else:
            print("Already commented on the newest good-first-issue.")
    
    return None
