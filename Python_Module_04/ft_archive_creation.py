print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")


class FileHandler:


    def __init__(self, file_name):
        self.file_name = file_name
        self.f_obj = None

    def open_file(self):
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

    def write_to_file(self):
        if self.f_obj is None:
            print("Oops! The file is Not existe")
        else:
            data = "{[}ENTRY 001{]} New quantum algorithm discovered"
                "{[}ENTRY 002{]} Efficiency increased by 347%"
                "{[}ENTRY 003{]} Archived by Data Archivist trainee"
            self.f_obj.write(data)
            self.f_obj.close()
            print("Data inscription complete. Storage unit sealed.")
            print(f"Archive '{self.file_name}' ready for long-term preservation.")


file = FileHandler("ancient_fragment.txt")

value = file.open_file()
if value is not None:
    file.read_file()
