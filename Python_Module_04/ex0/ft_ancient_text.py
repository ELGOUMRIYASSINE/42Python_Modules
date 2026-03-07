from abc import ABC

"""
CYBER ARCHIVES - DATA RECOVERY SYSTEM

A simple file handling system for recovering and reading archived data files.
"""

print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")


class FileHandler:
    """
    Manages opening and reading files with appropriate error handling
    and status messages.
    """
    def __init__(self, file_name):
        """
        Initialize the FileHandler.

        Args:
            file_name (str): The name of the file to handle.
        """
        self.file_name = file_name
        self.f_obj = None

    def open_file(self):
        """
        Attempt to open the specified file for reading.

        Returns:
            file object or None: The opened file object if successful,
                                 None if the file is not found.
        """
        print("Accessing Start")
        print("Searching for %s" % (self.file_name))

        try:
            self.f_obj = open(self.file_name, "r")
            print("Connection established...\n")
        except FileNotFoundError:
            print("Connection Fails: File Not Found !")
        return self.f_obj

    def read_file(self):
        """
        Read and display the contents of the opened file.

        Prints the file contents if available, or error messages if
        the file doesn't exist or is empty.
        """
        if self.f_obj is None:
            print("Oops! The file is Not existe")
        else:
            data = self.f_obj.read()
            if not data:
                print("Oops! The file is empty")
            else:
                print("RECOVERED DATA:")
                print(data)
                self.f_obj.close()
                print("\nData recovery complete. Storage unit disconnected.")


# file = FileHandler("ancient_fragment.txt")

# value = file.open_file()
# if value is not None:
#     file.read_file()
