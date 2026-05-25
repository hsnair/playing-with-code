import subprocess

# You need to have your current directory in Project-0
command = "nix-shell -p python3 python3Packages.pillow --run 'python3 maze.py maze2.txt'"
try:
    result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
    print("Command output:", result.stdout)
    print("Command errors:", result.stderr)
except subprocess.CalledProcessError as e:
    print("Command failed with error:", e)