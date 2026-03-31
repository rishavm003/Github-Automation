<div align="center">

<!-- Animated header banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a1a2e,100:16213e&height=200&section=header&text=GitHub%20Automator&fontSize=52&fontColor=58a6ff&animation=fadeIn&fontAlignY=38&desc=Your%20GitHub%20%E2%80%94%20on%20autopilot&descAlignY=58&descSize=18&descColor=8b949e" width="100%"/>

<!-- Animated typing SVG -->
<a href="https://github.com/YOUR_USERNAME/github-automator">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=22&pause=1000&color=58A6FF&center=true&vCenter=true&random=false&width=600&lines=Fully+automated+GitHub+activity+bot;AI-powered+issue+responses;Human-in-the-loop+draft+review;Green+contribution+graph+every+day;Set+once.+Run+forever." alt="Typing SVG" />
</a>

<br/>
<br/>

<!-- Core badges row -->
<img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
<img src="https://img.shields.io/badge/GitHub_Actions-automated-2088FF?style=for-the-badge&logo=github-actions&logoColor=white" alt="GitHub Actions"/>
<img src="https://img.shields.io/badge/AI_Powered-multi--provider-FF6B6B?style=for-the-badge&logo=openai&logoColor=white" alt="AI Powered"/>
<img src="https://img.shields.io/badge/Human_in_the_Loop-review_%26_approve-4CAF50?style=for-the-badge&logo=checkmarx&logoColor=white" alt="HITL"/>

<br/>
<br/>

<!-- Workflow status badge — replace YOUR_USERNAME/github-automator -->
<a href="https://github.com/YOUR_USERNAME/github-automator/actions/workflows/daily-run.yml">
  <img src="https://github.com/YOUR_USERNAME/github-automator/actions/workflows/daily-run.yml/badge.svg" alt="Daily Automation Status"/>
</a>
<img src="https://img.shields.io/github/last-commit/YOUR_USERNAME/github-automator?style=flat-square&color=58a6ff&label=last%20run" alt="Last Commit"/>
<img src="https://img.shields.io/github/license/YOUR_USERNAME/github-automator?style=flat-square&color=8b949e" alt="License"/>

</div>

---

<div align="center">

## ⚡ How it works

</div>

```
  Every day at 6:00 AM UTC — automatically, zero input from you
  ─────────────────────────────────────────────────────────────

  🤖 Bot wakes up
       │
       ├─► 📝  Commits daily log + motivational quote
       ├─► 📊  Updates README with live GitHub stats
       ├─► 🔍  Scans & scores good-first-issues across your target languages
       └─► 💬  Drafts AI replies to new issues in your own repos

       │
       ▼
  📋  Generates REVIEW.md with all drafts for your approval
       │
       ▼
  🔒  Commits everything → pushes to repo → waits for YOU

  ─────────────────────────────────────────────────────────────
  Your only job:

    git pull
    open REVIEW.md
    python approve_drafts.py   ← approve / edit / reject each draft
```

---

<div align="center">

## 🧠 What it automates

</div>

<table>
<tr>
<td width="50%">

### 📝 Daily Log Commit
Commits a dated log file to `logs/YYYY-MM-DD.md` every single day with a random dev quote and timestamp — keeping your contribution graph green **automatically**.

</td>
<td width="50%">

### 📊 README Stat Updater
Rebuilds your profile README daily with **live data** — repo count, total stars, forks, top languages, and your most-starred projects. Always fresh, never stale.

</td>
</tr>
<tr>
<td width="50%">

### 🔍 PR Opportunity Scanner
Finds the best `good-first-issue` tickets in your tech stack using a **smart scoring system** (stars, freshness, label quality, competition level). Drafts a genuine expression-of-interest comment for the top picks.

</td>
<td width="50%">

### 💬 AI Issue Responder
Scans your own repos for unanswered issues. Uses AI to draft a warm, context-aware reply — acknowledging the bug, feature request, or question in the right tone for that specific repo.

</td>
</tr>
</table>

---

<div align="center">

## 🤖 AI Provider Fallback Chain

<img src="https://skillicons.dev/icons?i=gcp" height="40" alt="Gemini"/> &nbsp;&nbsp;
<img src="https://img.shields.io/badge/→-gray?style=flat-square" height="20"/>
&nbsp;&nbsp;<img src="https://img.shields.io/badge/DeepSeek-0052CC?style=for-the-badge&logoColor=white" height="28" alt="DeepSeek"/>
&nbsp;&nbsp;<img src="https://img.shields.io/badge/→-gray?style=flat-square" height="20"/>
&nbsp;&nbsp;<img src="https://img.shields.io/badge/OpenRouter-8A2BE2?style=for-the-badge&logoColor=white" height="28" alt="OpenRouter"/>
&nbsp;&nbsp;<img src="https://img.shields.io/badge/→-gray?style=flat-square" height="20"/>
&nbsp;&nbsp;<img src="https://img.shields.io/badge/Claude-CC785C?style=for-the-badge&logo=anthropic&logoColor=white" height="28" alt="Claude"/>

</div>

```
Gemini 1.5 Flash  →  DeepSeek Chat  →  OpenRouter  →  Claude Haiku
```

The bot tries each provider **in order**. If one hits a rate limit (`429`) or auth error (`401/403`), it silently falls to the next. You only need **one valid API key** — the rest are backups. Each draft records which provider generated it.

---

<div align="center">

## 🛡️ Human-in-the-Loop Design

</div>

> The bot **never posts anything automatically.** Every comment goes through your review first.

```
┌─────────────────────────────────────────────────────────┐
│                     REVIEW.md                           │
│                                                         │
│  PR Comment Draft 1 — fastapi/fastapi                   │
│  Issue: Add example for background tasks in docs        │
│  Age: 0.3h  │  AI: Gemini  │  Score: 28.5              │
│                                                         │
│  ┌───────────────────────────────────────────────────┐  │
│  │ I'd love to contribute to this! I've worked with  │  │
│  │ FastAPI background tasks and could add a clear    │  │
│  │ example showing both fire-and-forget and tracked  │  │
│  │ patterns. Could I be assigned to this?            │  │
│  └───────────────────────────────────────────────────┘  │
│                                                         │
│  [A]pprove  [E]dit  [S]kip  [R]eject                   │
└─────────────────────────────────────────────────────────┘
```

**`approve_drafts.py` gives you full control:**

| Option | What it does |
|--------|-------------|
| `A` Approve | Post the draft exactly as-is |
| `E` Edit | Open in your `$EDITOR`, tweak the text, then post |
| `S` Skip | Keep the draft in queue for later |
| `R` Reject | Permanently discard |
| `Q` Quit | Come back later — nothing is lost |

---

<div align="center">

## 🚀 Setup

</div>

### Step 1 — Clone & push to your GitHub

```bash
git clone https://github.com/YOUR_USERNAME/github-automator
cd github-automator
# push to your own repo
```

### Step 2 — Add secrets

Go to your repo → **Settings → Secrets and variables → Actions → New repository secret**

| Secret | Required | Where to get it |
|--------|:--------:|----------------|
| `GEMINI_API_KEY` | One of these | [aistudio.google.com](https://aistudio.google.com) |
| `DEEPSEEK_API_KEY` | is required | [platform.deepseek.com](https://platform.deepseek.com) |
| `OPENROUTER_API_KEY` | at minimum | [openrouter.ai](https://openrouter.ai) |
| `ANTHROPIC_API_KEY` | optional | [console.anthropic.com](https://console.anthropic.com) |

> `GITHUB_TOKEN` is provided automatically — no action needed.

### Step 3 — (Optional) Set variables

**Settings → Variables → Actions → New repository variable**

| Variable | Default | Example |
|----------|---------|---------|
| `TARGET_LANGS` | `Python,JavaScript,TypeScript` | `Python,Go,Rust` |

### Step 4 — Set your local token (for approve_drafts.py)

```bash
# Windows
set GITHUB_TOKEN=ghp_your_token_here

# macOS / Linux
export GITHUB_TOKEN=ghp_your_token_here
```

### Step 5 — That's it. It runs itself.

The workflow triggers automatically at **6:00 AM UTC** every day. You can also check it fired correctly under the **Actions** tab.

---

<div align="center">

## 📂 Project Structure

</div>

```
github-automator/
│
├── 📁 .github/workflows/
│   └── daily-run.yml          ← ⏰ Cron: runs at 6 AM UTC daily
│
├── 📁 bot/
│   ├── ai_helper.py           ← 🧠 Gemini → DeepSeek → OpenRouter → Claude
│   ├── draft_manager.py       ← 🗂  Save, expire, deduplicate drafts
│   ├── issue_engager.py       ← 🔍 PR scanner + issue responder
│   ├── log_manager.py         ← 📝 Daily log with quote
│   ├── readme_updater.py      ← 📊 Live GitHub stats
│   └── report_generator.py   ← 📋 REVIEW.md + daily reports
│
├── 📁 config/
│   └── repo_tones.json        ← 🎭 Per-repo AI tone config
│
├── 📁 drafts/
│   └── pending.json           ← ⏳ All pending drafts (auto-managed)
│
├── 📁 logs/                   ← 📅 Daily log files (contribution streak)
├── 📁 reports/                ← 📊 Daily .md + .json reports
│
├── 📄 REVIEW.md               ← 👁  YOUR morning file — open this first
├── 🐍 approve_drafts.py       ← ✅ Your one command to push live
└── 📄 requirements.txt
```

---

<div align="center">

## 🔒 Draft Safety Features

</div>

<table>
<tr>
<td align="center" width="25%">
<br/>
<img src="https://img.shields.io/badge/⏰-48h_Stale_Warning-FFA500?style=for-the-badge" alt="stale"/>
<br/><br/>
Drafts over 48 hours get a <strong>⚠ STALE</strong> label in REVIEW.md
</td>
<td align="center" width="25%">
<br/>
<img src="https://img.shields.io/badge/🗑-72h_Auto_Discard-FF4444?style=for-the-badge" alt="expire"/>
<br/><br/>
Drafts over 72 hours are <strong>automatically removed</strong>
</td>
<td align="center" width="25%">
<br/>
<img src="https://img.shields.io/badge/🔁-Duplicate_Guard-4CAF50?style=for-the-badge" alt="dedup"/>
<br/><br/>
Never creates two drafts for the <strong>same issue URL</strong>
</td>
<td align="center" width="25%">
<br/>
<img src="https://img.shields.io/badge/⚡-Rate_Limit_Fallback-58A6FF?style=for-the-badge" alt="fallback"/>
<br/><br/>
Per-provider rate limit and auth error handling
</td>
</tr>
</table>

---

<div align="center">

## 🎭 Per-Repo Tone Config

</div>

Edit `config/repo_tones.json` to make AI responses feel natural for each repo:

```json
{
  "facebook/react":           "respectful and technically precise",
  "vercel/next.js":           "concise and professional",
  "your-username/serious-lib": "formal, detailed, and methodical",
  "your-username/fun-project": "casual, friendly, and enthusiastic"
}
```

The AI also reads issue **labels** automatically:
- `bug` label → empathetic, reassuring tone
- `feature` / `enhancement` → enthusiastic, constructive tone

---

<div align="center">

## 🛠️ Tech Stack

<br/>

<img src="https://skillicons.dev/icons?i=python,github,githubactions,vscode" height="50" alt="Tech Stack"/>

<br/><br/>

| Layer | Technology |
|-------|-----------|
| Language | Python 3.11+ |
| Automation | GitHub Actions (cron) |
| GitHub API | `PyGithub` + `requests` |
| AI | Gemini, DeepSeek, OpenRouter, Claude |
| Reports | `python-docx`, Markdown |
| Config | `python-dotenv` |

</div>

---

<div align="center">

## 📋 Your Daily Routine

</div>

```
🌅  Morning — bot already ran at 6 AM while you were asleep

  $ git pull
  $ cat REVIEW.md              # see what it prepared
  $ python approve_drafts.py   # approve, edit, or reject

  ✓  Done in under 2 minutes.
```

**Batch mode options:**

```bash
python approve_drafts.py              # Interactive (recommended)
python approve_drafts.py --all        # Approve everything at once
python approve_drafts.py --reject-all # Clear all drafts
python approve_drafts.py --dry-run    # Preview without posting
```

---

<div align="center">

## 📈 Contribution Graph Impact

<br/>

<img src="https://img.shields.io/badge/Daily_Commits-✓_Log_file-2ea44f?style=for-the-badge" alt="daily"/>
<img src="https://img.shields.io/badge/README_Updates-✓_Live_stats-2ea44f?style=for-the-badge" alt="readme"/>
<img src="https://img.shields.io/badge/Issue_Comments-✓_On_approval-2ea44f?style=for-the-badge" alt="comments"/>

<br/><br/>

Every day the bot guarantees **at least one commit** (the log file).
Approved drafts add more contribution activity throughout the day.

</div>

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:16213e,50:1a1a2e,100:0d1117&height=120&section=footer&animation=fadeIn" width="100%"/>

<br/>

**Built with 🤖 AI + ❤️ Human oversight**

<img src="https://img.shields.io/badge/Made%20with-Python-3776AB?style=flat-square&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Powered%20by-GitHub%20Actions-2088FF?style=flat-square&logo=github-actions&logoColor=white"/>
<img src="https://img.shields.io/badge/AI-Multi--Provider-FF6B6B?style=flat-square&logo=openai&logoColor=white"/>

<br/><br/>

*Replace `rishavm003` with your GitHub username before pushing.*

</div>
