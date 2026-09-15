from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent

# config dir (per-environment .env + secrets live here).
CONFIG_PATH = PROJECT_ROOT / "config"
