import os
import re
from github import Github

def update_readme_stats():
    token = os.getenv("GIT_TOKEN")
    if not token:
        print("GIT_TOKEN not set. Skipping README update.")
        return {"error": "No token"}

    g = Github(token)
    user = g.get_user()
    
    # Calculate simple stats
    repos = user.get_repos()
    total_stars = sum(repo.stargazers_count for repo in repos)
    total_repos = repos.totalCount

    stats_md = f"**Total Repositories:** {total_repos}\n**Total Stars:** {total_stars}\n"
    
    # Try updating local README.md
    readme_path = "README.md"
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Replace inside <!-- STATS:START --> and <!-- STATS:END -->
        pattern = r"<!-- STATS:START -->.*?<!-- STATS:END -->"
        replacement = f"<!-- STATS:START -->\n{stats_md}\n<!-- STATS:END -->"
        
        new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        
        print("Updated README.md with live stats.")
        return {"total_repos": total_repos, "total_stars": total_stars}
    else:
        print("README.md not found locally.")
        return {"error": "README not found"}
