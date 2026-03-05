from importlib import import_module
from importlib.metadata import version, PackageNotFoundError
import numpy as np

required_packages = {
    "requests":    ["2.31.0", "Network access ready"],
    "pandas":      ["2.1.0",  "Data manipulation ready"],
    "matplotlib":  ["3.7.0",  "Visualization ready"],
}

def check_dependencies():
    print("Checking dependencies...")
    for package, (required_version, message) in required_packages.items():
        try:
            import_module(package)
            print(f"[OK] {package} ({required_version}) - {message}")
        except ImportError:
            print(f"[MISSING] {package} - Please install dependencies:")
            print(f"  pip install -r requirements.txt")
            print(f"  # or: poetry install")
            exit(1)
        except PackageNotFoundError:
            print(f"[NOT FOUND] {package} metadata not available")
            exit(1)

print("LOADING STATUS: Loading programs...\n")
check_dependencies()

import pandas as pd
import matplotlib.pyplot as plt
import requests

print("Analyzing Matrix data...")
response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=33.57&longitude=-7.59&hourly=temperature_2m")
data = response.json()
time = data["hourly"]["time"]
temp = data["hourly"]["temperature_2m"]

data = pd.DataFrame(
    {
        "time": time,
        "temperature": temp
    }
)

print(f"Processing {len(data)} data points...")
plt.plot(data["time"], data["temperature"])
plt.title(f"Processing {len(data)} data points...")
plt.xlabel("Time")
plt.ylabel("Temperature")
print("Generating visualization...")
plt.savefig("matrix_analysis.png")
print("Analysis complete!")
print(f"Results saved to: {os.path.abspath('matrix_analysis.png')}")
