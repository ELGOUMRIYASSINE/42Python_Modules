import sys
import os
import site

if sys.prefix == sys.base_prefix:
    print("\nMATRIX STATUS: You're still plugged in.\n")
else:   
    print("\nMATRIX STATUS:  Welcome to the construct\n")

print("Current Python:", sys.executable)
print("Virtual Environment:", os.path.basename(sys.prefix) if sys.prefix != sys.base_prefix else "None detected")
if sys.prefix == sys.base_prefix:
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
   print(f"Environment Path: {sys.prefix}\n")
   print("SUCCESS: You're in an isolated environment!")
   print("Safe to install packages without affecting the global system.\n")
   print("Package installation path:", site.getsitepackages()[0])
