class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def test_exceptions():
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
        print("Caught a garden error:  Not enough water in the tank!\n")

    print("All custom error types work correctly!")


test_exceptions()
