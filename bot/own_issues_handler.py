import os
from github import Github
from anthropic import Anthropic

def handle_own_issues():
    github_token = os.getenv("GITHUB_TOKEN")
    anthropic_key = os.getenv("ANTHROPIC_API_KEY")
    
    if not github_token or not anthropic_key:
        print("Missing API keys. Skipping own issue handler.")
        return []

    g = Github(github_token)
    client = Anthropic(api_key=anthropic_key)
    user = g.get_user()
    
    responses = []
    
    # Get recent issues in owned repos
    for repo in user.get_repos(type="owner"):
        issues = repo.get_issues(state="open")
        for issue in issues[:5]: # limit to 5 to avoid heavy API usage
            # If no comments except the creator's, or just new issue
            if issue.comments == 0:
                print(f"Drafting response for issue {issue.title} in {repo.name}")
                
                # Use Claude to draft a friendly reply
                prompt = f"Write a short, friendly open-source maintainer reply acknowledging this new issue:\nTitle: {issue.title}\nBody: {issue.body}\nDo not include any placeholders, just the comment text."
                
                try:
                    response = client.messages.create(
                        model="claude-3-haiku-20240307",
                        max_tokens=200,
                        messages=[{"role": "user", "content": prompt}]
                    )
                    draft_reply = response.content[0].text
                    
                    # Instead of auto-posting (which might be risky depending on what Claude says),
                    # we can post it with a draft prefix for review or auto-post if specified.
                    # Posting it right away according to prompt "Uses Claude API to draft and post friendly replies."
                    
                    issue.create_comment(f"*(Auto-drafted by Claude)*\n{draft_reply}")
                    
                    responses.append({
                        "repo": repo.name,
                        "issue_title": issue.title,
                        "url": issue.html_url,
                        "draft": draft_reply
                    })
                except Exception as e:
                    print(f"Error calling Claude: {e}")
                    
    return responses
