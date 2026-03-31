import os
import datetime
from dotenv import load_dotenv

load_dotenv()
import datetime
from bot.log_manager import write_daily_log
from bot.readme_updater import update_readme_stats
from bot.issue_engager import engage_good_first_issue, handle_own_repo_issues
from bot.report_generator import generate_reports
from bot.draft_manager import save_draft

def main():
    print("Starting GitHub Daily Automation Bot")
    now_utc = datetime.datetime.now(datetime.timezone.utc)
    timestamp = now_utc.strftime("%Y-%m-%dT%H:%M:%SZ")
    date_str = now_utc.strftime("%Y-%m-%d")

    day_artifacts = {}

    # 1. Log with quote
    log_file, quote_data = write_daily_log(date_str, timestamp)
    day_artifacts["quote"] = quote_data
    day_artifacts["log_file"] = log_file

    # 2. Update Profile README
    stats = update_readme_stats()
    day_artifacts["readme_stats"] = stats

    # 3. Good First Issues
    gfi_action = engage_good_first_issue()
    day_artifacts["good_first_issue"] = gfi_action
    if gfi_action:
        save_draft(gfi_action["type"], "Unknown (Search)", gfi_action["url"], gfi_action["title"], gfi_action["draft"])

    # 4. AI Replies to Own Issues
    claude_responses = handle_own_repo_issues()
    day_artifacts["claude_responses"] = claude_responses
    for resp in claude_responses:
        save_draft(resp["type"], resp["repo"], resp["url"], resp["issue_title"], resp["draft"])

    # 5. Generate Reports
    md_report, docx_report = generate_reports(date_str, timestamp, day_artifacts)
    print(f"Generated reports: {md_report}, {docx_report}")
    
    if gfi_action or claude_responses:
        print("\n[!] DRAFTS GENERATED: Run 'python approve_drafts.py' to review and post comments.")

if __name__ == "__main__":
    main()
