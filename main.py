import os
import datetime
from dotenv import load_dotenv

load_dotenv()
from bot.log_manager import write_daily_log
from bot.issue_engager import engage_good_first_issue, handle_own_repo_issues
from bot.report_generator import generate_reports, generate_review_md
from bot.draft_manager import save_draft, load_all_drafts

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

    # 2. Good First Issues
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
    
    # 6. Generate/Update REVIEW.md
    all_drafts = load_all_drafts()
    generate_review_md(all_drafts)
    
    if gfi_action or claude_responses:
        print(f"\n[!] {len(all_drafts)} DRAFTS PENDING: Review 'REVIEW.md' and run 'python approve_drafts.py'.")

if __name__ == "__main__":
    main()
