def garden_operations(type_error):
    """
    Simulates various types of errors based on the input value.

    Args:
        type_error: An integer specifying which error to simulate.
                    1 - ValueError
                    2 - ZeroDivisionError
                    3 - FileNotFoundError
                    4 - KeyError
                    5 - Multiple errors
    """
    if (type_error == 1):
        print("Testing ValueError...")
        x = int("abc")
    elif (type_error == 2):
        print("Testing ZeroDivisionError...")
        x = 10/0
    elif (type_error == 3):
        print("Testing FileNotFoundError...")
        x = open("yassine.txt", "r")
    elif (type_error == 4):
        print("Testing KeyError..")
        test = {
            "name": "yassine",
            "age": 19
        }
        x = test["type_errorry"]
    else:
        print("Testing multiple errors together...")
        x = int("abc")
        x = 10/0
        x = open("yassine.txt", "r")
        test = {
            "name": "yassine",
            "age": 19
        }
        x = test["type_errorry"]
        return (x)


def test_error_types():
    """
    Tests different types of errors by calling `garden_operations`.

    Catches specific exceptions for each error type and prints a message.
    """
    try:
        garden_operations(1)
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")

    try:
        garden_operations(2)
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")

    try:
        garden_operations(3)
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")

    try:
        garden_operations(4)
    except KeyError:
        print("Caught KeyError: 'missing\\_plant' \n")

    try:
        garden_operations(5)
    except Exception:
        print("Caught an error, but program continues!\n")

    print("All error types tested successfully!")


test_error_types()
