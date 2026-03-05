# construct.py
# Simple utility that reports whether this Python process is running
# inside a virtual environment (venv) or the global interpreter.

import sys
import os
import site

# If sys.prefix equals sys.base_prefix, Python is running in the global
# (system) environment. When different, we are inside a virtual environment.
if sys.prefix == sys.base_prefix:
    # Not inside a venv
    print("\nMATRIX STATUS: You're still plugged in.\n")
else:
    # Inside a virtual environment
    print("\nMATRIX STATUS:  Welcome to the construct\n")

# Show which Python executable is in use
print("Current Python:", sys.executable)

# Show the name of the virtual environment if present, otherwise say none
print(
    "Virtual Environment:",
    os.path.basename(sys.prefix) if sys.prefix != sys.base_prefix else "None detected",
)

if sys.prefix == sys.base_prefix:
    # Give guidance for creating and activating a virtual environment
    print("\nWARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env")
    print("Scripts")
    print("activate # On Windows\n")
    print("Then run this program again.")
else:
    # In a venv — show path details and where packages will be installed
    print(f"Environment Path: {sys.prefix}\n")
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.\n")
    # site.getsitepackages()[0] is typically where pip installs packages
    print("Package installation path:", site.getsitepackages()[0])
