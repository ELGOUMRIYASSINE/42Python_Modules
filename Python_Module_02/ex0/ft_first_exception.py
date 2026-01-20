def check_temperature(temp_str):
    """ exception handling to handle if any error appears"""
    try:
        number = int(temp_str)
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
    """ test  check_temperature systeme if the tests completed and no crash"""
    print("=== Garden Temperature Checker ===\n")
    tests = ["25", "abc", "100", "-50"]
    for i in tests:
        print(f"Testing temperature: {i}")
        check_temperature(i)
    print("All tests completed - program didn't crash!")


test_temperature_input()
