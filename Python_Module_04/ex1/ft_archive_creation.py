print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")


class FileHandler:
    """Handles file creation and data storage operations."""

    def __init__(self, file_name):
        """Initialize with a filename to work with."""
        self.file_name = file_name
        self.f_obj = None

    def open_file(self):
        """Open a new file for writing. Returns file object or None if it
        fails."""
        print(f"Initializing new storage unit: {self.file_name}")

        try:
            self.f_obj = open(self.file_name, "w")
            print("Storage unit created successfully...\n")
        except FileNotFoundError:
            print("Error: Directory does not exist (FileNotFoundError)")
        except PermissionError:
            print("Error: No permission to write (PermissionError)")
        except IsADirectoryError:
            print("Error: Tried to open a directory (IsADirectoryError)")
        except (OSError, IOError):
            print("Error: OS error occurred (disk full, read-only, etc.)")
        except Exception as e:
            print(f"Unexpected error: {e}")
        return self.f_obj

    def write_to_file(self, data):
        """Write data to the file and close it."""
        try:
            if self.f_obj is None:
                print("Oops! The file is Not existe")
            else:
                print("Inscribing preservation data...")
                print(data)
                self.f_obj.write(data)
                self.f_obj.close()
                print("Data inscription complete. Storage unit sealed.")
                name = self.file_name
                print(f"Archive '{name}' ready for long-term preservation.")
        # the file can be closed after we open it directly on the open file
        # function so f_obj will still hold a not None Value
        except ValueError:
            print("Oops !: somthing wrong check is the file open")


file = FileHandler("new_discovery.txt")
data = "[ENTRY 001] New quantum algorithm discovered\n"\
       "[ENTRY 002] Efficiency increased by 347%\n"\
       "[ENTRY 003] Archived by Data Archivist trainee\n"
value = file.open_file()
if value is not None:
    file.write_to_file(data)
