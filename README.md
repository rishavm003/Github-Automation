# GitHub Daily Automation Bot

This repository houses the Python scripts and GitHub Action workflow for the Daily Automation Bot.

## Overview
- Commits a daily log with a timestamp and a quote
- Automatically updates the profile repo stats here in the README
- Scans `good-first-issue` on GitHub and posts interest
- Uses Claude API to generate and post draft replies to issues opened in the owner's repos
- Generates `.md` and `.docx` report artifacts detailing all automation executed daily

## Stats
<!-- STATS:START -->
*Stats will be populated automatically by GitHub Actions.*
<!-- STATS:END -->

## Setup
1. Define repository secrets: `ANTHROPIC_API_KEY`
2. Ensure `GITHUB_TOKEN` has read/write permissions for repo contents and issues.
