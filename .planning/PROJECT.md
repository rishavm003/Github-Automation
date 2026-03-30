# GitHub Daily Automation Bot

## What This Is
A fully automated daily GitHub manager that handles routine engagement (issue commenting, quote logging) and daily reporting (Markdown and Docx artifacts) using GitHub Actions and Claude.

## Core Value
To maintain an active, engaging GitHub profile by consistently scanning, reviewing, and tracking issues entirely automatically on a 6 AM UTC cron schedule.

## Requirements

### Active
- [ ] Log file commit with daily quote and timestamp
- [ ] Auto-update profile README with live repo stats
- [ ] Good-first-issue scanner and auto-comment in Python/JavaScript
- [ ] Claude-powered automated responses to new issues in own repos
- [ ] Daily report generated in Markdown and Docx (tasks, stats, PRs, draft responses, artifacts list)
- [ ] Triggered by GitHub Actions cron at 6 AM UTC
- [ ] Logs and artifacts committed back automatically

### Out of Scope
- Interacting with PR code review (bot focuses only on issues and generic quotes).
