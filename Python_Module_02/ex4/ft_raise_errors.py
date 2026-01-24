def check_plant_health(plant_name, water_level, sunlight_hours):
    """
    Validates a plant's name, water level, and sunlight hours.

    Args:
        plant_name: The name of the plant.
        water_level: A value between 1 and 10.
        sunlight_hours: A value between 2 and 12.

    Raises:
        ValueError: If the inputs are invalid.
    """
    if (plant_name == ""):
        raise ValueError("Error: Plant name cannot be empty!\n")
    elif (not (water_level >= 1 and water_level <= 10)):

        if (water_level < 1):
            raise ValueError(f"Error: Water level"
                             f" {water_level} is too low (min 1)\n")
        else:
            raise ValueError(f"Error: Water level"
                             f" {water_level} is too high (max 10)\n")

    elif (not (sunlight_hours >= 2 and sunlight_hours <= 12)):
        if (sunlight_hours < 2):
            raise ValueError(f"Error: Sunlight hours "
                             f"{sunlight_hours} is too low (min 2)\n")
        else:
            raise ValueError(f"Error: Sunlight hours "
                             f"{sunlight_hours} is too high (max 12)\n")
    else:
        print(f"Success! Your {plant_name} plant pass the test\n")


def test_plant_checks():
    """
    Tests the plant health validation function with different values.
    """
    print("=== Garden Plant Health Checker ===\n")
    try:
        print("Testing good values...")
        check_plant_health("dela7", 8, 3)
    except ValueError as e:
        print(e)

    try:
        print("Testing empty plant name...")
        check_plant_health("", 8, 3)
    except ValueError as e:
        print(e)

    try:
        print("Testing bad water level...")
        check_plant_health("maticha", 20, 3)
    except ValueError as e:
        print(e)

    try:
        print("Testing bad sunlight hours...")
        check_plant_health("maticha", 8, -60)
    except ValueError as e:
        print(e)

    print("All error raising tests completed!")


test_plant_checks()
