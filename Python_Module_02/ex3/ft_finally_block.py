class Error(Exception):
    """
    Custom error class for the watering system.
    """
    pass


def water_plants(plant_list):
    """
    Waters the plants in the provided list.

    Args:
        plant_list: A list of plant names.

    Raises:
        Error: If an element in the list is not a valid string.
    """
    print("Opening watering system")
    for plant in plant_list:
        if plant and isinstance(plant, str):
            print(f"Watering {plant}")
        else:
            raise Error


def test_watering_system():
    """
    Tests the watering system with different plant lists.
    """
    good_list = ["tomato", "jelbana", "batata", "dela7"]
    print("=== Garden Watering System ===")
    print("Testing normal watering...")
    try:
        water_plants(good_list)
        print("Watering completed successfully!")
    except Error:
        print("Error: Cannot water None - invalid plant!")
    finally:
        print("Closing watering system (cleanup)\n")

    print("Testing abnormal watering...")
    good_list = ["tomato", 120, "batata", "dela7"]
    try:
        water_plants(good_list)
        print("Watering completed successfully!")
    except Error:
        print("Error: Cannot water None - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


test_watering_system()
