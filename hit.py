import socket
import subprocess
import sys
import time
import webbrowser
from pathlib import Path

app_path = Path(__file__).resolve().parent / "cfl.py"
with socket.socket() as port_socket:
    port_socket.bind(("127.0.0.1", 0))
    port = port_socket.getsockname()[1]

app_url = f"http://localhost:{port}"
command = [
    sys.executable,
    "-m",
    "streamlit",
    "run",
    str(app_path),
    f"--server.port={port}",
    "--server.headless=true",
]

print(">>> Starting Streamlit runner...", flush=True)
process = subprocess.Popen(command)

try:
    for _ in range(60):
        if process.poll() is not None:
            raise subprocess.CalledProcessError(process.returncode, command)

        try:
            with socket.create_connection(("127.0.0.1", port), timeout=1):
                break
        except OSError:
            time.sleep(0.5)
    else:
        raise TimeoutError("Streamlit did not start within 30 seconds.")

    if not webbrowser.open(app_url):
        print(f"Open this URL in your browser: {app_url}")

    process.wait()
finally:
    if process.poll() is None:
        process.terminate()