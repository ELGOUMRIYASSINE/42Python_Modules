"""Communication system for managing Archive data streams."""
import sys


def send_to_channels(id, status_report):
    """Send messages to appropriate channels: stdout and stderr."""
    sys.stdout.write(
        "\n{[}STANDARD{]} Archive status from %s: %s\n" % (
            id, status_report))
    sys.stderr.write(
        "{[}ALERT{]} System diagnostic: Communication channels verified\n")
    sys.stdout.write("{[}STANDARD{]} Data transmission complete\n")


print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

id = input("Input Stream active. Enter archivist ID: ")
status_report = input("Input Stream active. Enter status report: ")

send_to_channels(id, status_report)
print("\nThree-channel communication test successful")
