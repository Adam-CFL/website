import subprocess
import sys
from pathlib import Path
from streamlit.web.cli import main
print(">>> Starting Streamlit runner via subprocess...")

app_path = Path(__file__).resolve().parent / "cfl"
subprocess.run([sys.executable, "-m", "streamlit", "run", str(app_path)])