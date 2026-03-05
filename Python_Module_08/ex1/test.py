# Script purpose: verify required packages, fetch gold price data, and generate a plot.

from importlib.util import find_spec  # Used to check if a package exists in the environment.
from importlib.metadata import version  # Used to read installed package versions.
import sys  # Used to exit the script when a dependency is missing.

# Human-readable dependency list used during startup checks.
dependencies = [
    ('pandas', 'Data manipulation'),
    ('requests', 'Network access'),
    ('matplotlib', 'Visualization'),
]

def checking_dependencies(dependencies: list):
    # Validate that each required package is installed before continuing.
    for pkg, msg in dependencies:
        package = find_spec(pkg)
        if package is not None:
            # Package is available; print detected version and capability.
            print(f"[OK] {package.name} ({version(package.name)}) - {msg} ready")
        else:
            # Package missing; print quick setup instructions then exit.
            print(f"[MISSING] {pkg} - {msg} not ready")
            print("\nTry:")
            print("pip install -r requirements.txt")
            print("python3 loading.py")
            print("Or")
            print("poetry install")
            print("poetry run python loading.py")
            sys.exit()

# Startup banner and dependency verification.
print("\nLOADING STATUS: Loading programs...\n")
print("Checking dependencies:")
checking_dependencies(dependencies)  # Run dependency checks.

# Import runtime dependencies after validation passes.
import pandas
import requests
import matplotlib.pyplot

# Gold daily CSV endpoint (XAU/USD)
URL = "https://stooq.com/q/d/l/?s=xauusd&i=d"

# Download CSV text from endpoint and split into lines.
raw_csv = requests.get(URL).text.strip().splitlines()

# Parse CSV rows (skip header), keeping only non-empty lines.
prices = [line.split(",") for line in raw_csv[1:] if line.strip()]

print("\nAnalyzing Matrix data...")

# Build numeric values, extract the 'Close' price (5th column) from each row, converting to numeric.
values = pandas.to_numeric(
    [p[4] for p in prices if len(p) > 4 and p[4]])

print(f"Processing {len(values)} data points...")

# Create and style the chart for exported analysis.
matplotlib.pyplot.figure(figsize=(10, 5))
matplotlib.pyplot.plot(values)
matplotlib.pyplot.title("Gold Price (XAU/USD)")
matplotlib.pyplot.xlabel("Time")
matplotlib.pyplot.ylabel("Price (USD)")
matplotlib.pyplot.grid()

# Output filename for generated chart image.
image = "matrix_analysis.png"
print("Generating visualization...")

# Save image and release plotting resources.
matplotlib.pyplot.savefig(image, dpi=100, facecolor='white')
matplotlib.pyplot.close()

# Final completion message.
print("\nAnalysis complete!")
print(f"Results saved to: {image}")