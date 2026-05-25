import subprocess

commands = [
    "python3 -m venv .venv",
    "source .venv/bin/activate",
    "pip install -r requirements.txt"
]

for command in commands:
    process = subprocess.run(command, shell=True, check=True)
    print(f"Command '{command}' finished with exit code {process.returncode}")