import os

# Base paths
BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
LOGS_DIR = os.path.join(DATA_DIR, "logs")
REPORTS_DIR = os.path.join(DATA_DIR, "reports")
DRAFTS_DIR = os.path.join(DATA_DIR, "drafts")

# File paths
DRAFTS_FILE = os.path.join(DRAFTS_DIR, "pending.json")
README_FILE = os.path.join(BASE_DIR, "README.md")
REVIEW_FILE = os.path.join(BASE_DIR, "REVIEW.md")
REPO_TONES_FILE = os.path.join(BASE_DIR, "config", "repo_tones.json")

# Ensure directories exist
def ensure_dirs():
    for d in [LOGS_DIR, REPORTS_DIR, DRAFTS_DIR]:
        os.makedirs(d, exist_ok=True)
