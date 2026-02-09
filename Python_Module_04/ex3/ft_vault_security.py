def secure_log():
    """Simulates vault access by reading, displaying, and overwriting a
    file."""
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols\n")

    print("SECURE EXTRACTION:")
    with open("ancient_fragment.txt", "r") as fl:
        content = fl.read()
        print(content)
        print()

    print("SECURE PRESERVATION:")
    with open("ancient_fragment.txt", "w") as fl:
        content = fl.write("[CLASSIFIED] New security protocols archived")
        print("[CLASSIFIED] New security protocols archived")
        print("Vault automatically sealed upon completion\n")

    print("All vault operations completed with maximum security.")


print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
secure_log()
