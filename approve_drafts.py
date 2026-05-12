import os
import json
from github import Github
from dotenv import load_dotenv
from bot.draft_manager import load_all_drafts, clear_drafts

def main():
    load_dotenv()
    token = os.getenv("GITHUB_TOKEN") or os.getenv("GIT_TOKEN")
    if not token:
        print("GITHUB_TOKEN or GIT_TOKEN not set in .env")
        return

    drafts = load_all_drafts()
    if not drafts:
        print("No pending drafts to review.")
        return

    g = Github(token)
    print(f"--- Reviewing {len(drafts)} Pending AI Comments ---\n")
    
    approved_count = 0
    remaining_drafts = []

    for item in drafts:
        print(f"Target: {item['url']}")
        print(f"Repo: {item['repo']}")
        print(f"Title: {item['title']}\n")
        print(f"--- PROPOSED COMMENT ---")
        print(item['draft'])
        print(f"------------------------\n")
        
        choice = input("Post this comment? (y = Yes, n = No/Skip, q = Quit): ").lower()
        
        if choice == 'y':
            try:
                # Extract repo owner/name from URL
                # Example: https://github.com/user/repo/issues/1
                url_parts = item['url'].split("/")
                repo_full_name = f"{url_parts[3]}/{url_parts[4]}"
                issue_number = int(url_parts[6])
                
                repo = g.get_repo(repo_full_name)
                issue = repo.get_issue(number=issue_number)
                
                issue.create_comment(item['draft'])
                print(f"Successfully posted to {item['url']}")
                approved_count += 1
            except Exception as e:
                print(f"Failed to post comment: {e}")
                remaining_drafts.append(item)
        elif choice == 'q':
            remaining_drafts.extend(drafts[drafts.index(item):])
            break
        else:
            print("Skipped.")
            remaining_drafts.append(item)
        
        print("\n" + "="*40 + "\n")

    # Update the drafts file with only the remaining ones
    if not remaining_drafts:
        clear_drafts()
    else:
        with open("data/drafts/pending.json", "w", encoding="utf-8") as f:
            json.dump(remaining_drafts, f, indent=4)

    print(f"Review session finished. {approved_count} comments posted.")

if __name__ == "__main__":
    main()
