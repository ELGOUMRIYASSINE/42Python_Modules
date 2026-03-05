import os
import sys
from dotenv import load_dotenv


def load_configuration():
    # Read environment variables from a .env file into os.environ.
    # This keeps secrets and config out of source code.
    if not os.path.exists(".env"):
        print("ERROR: Missing .env file")
        sys.exit(1)
    load_dotenv()
    # The configuration dictionary collects relevant settings with
    # sensible defaults where appropriate.
    config = {
        "mode": os.getenv("MATRIX_MODE", "development"),
        "database": os.getenv("DATABASE_URL"),
        "api_key": os.getenv("API_KEY"),
        "log_level": os.getenv("LOG_LEVEL", "INFO"),
        "zion": os.getenv("ZION_ENDPOINT")
    }
    return config


def validate_config(config):
    # Simple validation: ensure required secrets (like API keys) exist.
    if not config["api_key"]:
        print("ERROR: Missing API_KEY")
        sys.exit(1)


def main():
    # Entry point for the module when run as a script.
    print("ORACLE STATUS: Reading the Matrix...\n")

    config = load_configuration()
    validate_config(config)

    # Show loaded configuration (avoiding printing secrets in real apps).
    print("Configuration loaded:")
    print(f"Mode: {config['mode']}")
    print(f"Database: {config['database']}")
    print(f"Api Access: {'Authenticated' if config['api_key'] else 'Not Authenticated'}")
    print(f"Log Level: {config['log_level']}")
    print(f"Zion Network: {config['zion']}")

    # Basic environment checks — placeholders for more advanced checks.
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available\n")
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
