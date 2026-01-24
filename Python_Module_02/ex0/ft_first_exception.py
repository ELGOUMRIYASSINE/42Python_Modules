def check_temperature(temp_str):
    """
    Checks if the given temperature is suitable for plants.

    Args:
        temp_str: The temperature as a string input.

    Returns:
        The temperature as an integer if it is in the valid range (0-40°C).

    Prints:
        Error messages if the temperature is too cold, too hot,
        or if the input is invalid.

    Handles:
        Exception if the input is not a valid integer.
    """
    try:
        number = int(temp_str)  # Convert string to integer
        if (number < 0):
            print(f"Error: {number}°C is too cold for plants (min 0°C)\n")
        elif (number > 40):
            print(f"Error: {number}°C is too hot for plants (max 40°C)\n")
        else:
            print(f"Temperature {number}°C is perfect for plants!\n")
            return (number)
    except Exception:
        print(f"Error: '{temp_str}' is not a valid number\n")


def test_temperature_input():
    """
    Tests the temperature checking system with multiple inputs.

    Ensures the function handles valid temperatures, out-of-range inputs,
    and invalid strings without crashing.
    """
    print("=== Garden Temperature Checker ===\n")
    tests = ["25", "abc", "100", "-50"]
    for i in tests:
        print(f"Testing temperature: {i}")
        check_temperature(i)
    print("All tests completed - program didn't crash!")


test_temperature_input()
