import sys
from pathlib import Path

# Add the project root (6jan2025) to sys.path
PROJECT_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(PROJECT_ROOT))
