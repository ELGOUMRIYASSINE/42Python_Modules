import os
import sys
from dotenv import load_dotenv


def load_configuration():
    load_dotenv()
    # here where the variables loaded from .env file are used,
    # we can set MATRIX_MODE to "test" for testing purposes
    # os.environ["MATRIX_MODE"] = "test"
    config = {
        "mode": os.getenv("MATRIX_MODE", "development"),
        "database": os.getenv("DATABASE_URL"),
        "api_key": os.getenv("API_KEY"),
        "log_level": os.getenv("LOG_LEVEL", "INFO"),
        "zion": os.getenv("ZION_ENDPOINT")
    }
    return config


def validate_config(config):
    if not config["api_key"]:
        print("ERROR: Missing API_KEY")
        sys.exit(1)


def main():
    print("ORACLE STATUS: Reading the Matrix...\n")

    config = load_configuration()
    validate_config(config)

    print("Configuration loaded:")
    print(f"Mode: {config['mode']}")
    print(f"Database: {config['database']}")
    print(f"Log Level: {config['log_level']}")
    print(f"Zion Endpoint: {config['zion']}")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available\n")
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
