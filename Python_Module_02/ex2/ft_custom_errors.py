class GardenError(Exception):
    """
    Base class for all garden-related errors.
    """
    pass


class PlantError(GardenError):
    """
    Raised when there is a problem with the plants.
    """
    pass


class WaterError(GardenError):
    """
    Raised when there is a problem with the water supply.
    """
    pass


def test_exceptions():
    """
    Tests the custom exception classes to ensure they work correctly.
    """
    print("=== Custom Garden Errors Demo ===\n")

    try:
        print("Testing PlantError...")
        raise PlantError
    except PlantError:
        print("Caught PlantError: The plants is wilting!\n")

    try:
        print("Testing WaterError...")
        raise WaterError
    except WaterError:
        print("Caught WaterError: Not enough water in the tank!\n")

    try:
        print("Testing catching all garden errors...")
        raise GardenError
    except GardenError:
        print("Caught a garden error: The plants is wilting!")
        print("Caught a garden error: Not enough water in the tank!\n")

    print("All custom error types work correctly!")


test_exceptions()
