import os
import re
from github import Github
from bot.config import README_FILE, ensure_dirs

def update_readme_stats():
    token = os.getenv("GITHUB_TOKEN") or os.getenv("GIT_TOKEN")
    if not token:
        print("GITHUB_TOKEN or GIT_TOKEN not set. Skipping README update.")
        return {"error": "No token"}

    g = Github(token)
    try:
        user = g.get_user()
        # Calculate simple stats
        repos = user.get_repos()
        total_stars = sum(repo.stargazers_count for repo in repos)
        total_repos = repos.totalCount
    except Exception as e:
        print(f"Error fetching GitHub stats: {e}")
        return {"error": str(e)}

    stats_md = f"**Total Repositories:** {total_repos}\n**Total Stars:** {total_stars}\n"

    # Try updating local README.md
    if os.path.exists(README_FILE):
        with open(README_FILE, "r", encoding="utf-8") as f:
            content = f.read()
        
        # ... (same)
        pattern = r"<!-- STATS:START -->.*?<!-- STATS:END -->"
        replacement = f"<!-- STATS:START -->\n{stats_md}\n<!-- STATS:END -->"
        
        new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        
        with open(README_FILE, "w", encoding="utf-8") as f:
            f.write(new_content)
        
        print("Updated README.md with live stats.")
        return {"total_repos": total_repos, "total_stars": total_stars}
    else:
        print("README.md not found locally.")
        return {"error": "README not found"}
