def Crisi_log(state, archive):
    """Attempts to read a file and handles common errors gracefully."""
    try:
        print(f"{state}: Attempting access to '{archive}'...")
        with open(archive) as file:
            print(f"SUCCESS: Archive recovered - ``{file.read()}''")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    except Exception as e:
        print(f"Unexpected error: {e}")


print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

Crisi_log("CRISIS ALERT", "lost_archive.txt")
print()
Crisi_log("CRISIS ALERT", "classified_vault.txt")
print()
Crisi_log("ROUTINE ACCESS", "standard_archive.txt")


print("\nAll crisis scenarios handled successfully. Archives secure.")
