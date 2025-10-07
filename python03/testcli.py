import subprocess
import sys

# Check if the user provided a command
if len(sys.argv) < 2:
    print("Usage: python test_command.py \"command to run\"")
    sys.exit(1)

# Join the command arguments
command = sys.argv[1:]

try:
    result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print("✅ Command executed successfully.")
    print("Output:\n", result.stdout)
except subprocess.CalledProcessError as e:
    print("❌ Command failed with error code:", e.returncode)
    print("Error output:\n", e.stderr)
except FileNotFoundError:
    print("❌ Command not found.")
