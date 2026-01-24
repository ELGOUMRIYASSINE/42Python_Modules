"""
This script demonstrates how to work with command-line arguments in Python.

- It first checks if any arguments were passed to the script.
- It prints the program name (the script itself).
- If arguments are provided, it displays how many were received and lists
  each argument.
- It helps you understand how to use `sys.argv`.

To run:
1. Save this script to a file, for example, `command_quest.py`.
2. Execute it in the terminal: `python command_quest.py arg1 arg2`.

Purpose:
The script shows how to handle and display command-line input using `sys.argv`.
"""

import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    number_of_argv = len(sys.argv)
    if (number_of_argv < 2):
        print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")
    if (number_of_argv > 1):
        print(f"Arguments received: {number_of_argv - 1}")
        i = 1
        while (i < number_of_argv):
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
    print(f"Total arguments: {number_of_argv}")
