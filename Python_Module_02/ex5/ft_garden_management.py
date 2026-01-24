class GardenError(Exception):
    """Base class for all garden-related errors"""
    pass


class PlantError(GardenError):
    """Raised when there is an issue adding a plant"""

    def __str__(self):
        return "Error adding plant: Plant name cannot be empty!\n"


class WaterError(GardenError):
    """Raised when there is an issue with water levels"""
    pass


class GardenManager:
    """Manages the plants, water supply, and health of the garden"""

    adding_process = 0

    def __init__(self, tank):
        """Initializes the GardenManager with a water tank
        and an empty plant list"""
        self.plants = []
        self.tank = tank

    def add(self, object):
        """Adds a plant to the garden"""
        try:
            if (self.adding_process == 0):
                print("Adding plants to garden...")
            if (object.name == ""):
                raise PlantError
            else:
                self.plants.append(object)
                print(f"Added {object.name} successfully")
                self.adding_process += 1
        except PlantError as e:
            print(e)

    def water_plants(self):
        """Waters all plants in the garden, raises an error if
        there is not enough water"""
        print("Watering plants...")
        try:
            if self.tank <= 0:
                raise GardenError("Error: Not enough water in tank")
            print("Opening watering system")
            for plant in self.plants:
                if self.tank <= 0:
                    raise GardenError("Error: Not enough water in tank")
                plant.water += 1
                self.tank -= 1
                print(f"Watering {plant.name} - success")
        except GardenError as e:
            print(e)
        finally:
            print("Closing watering system\n")

    def check_health(self):
        """Checks the health of all plants based on water and
        sunlight levels"""
        try:
            print("Checking plant health...")
            for plant in self.plants:
                if (not (plant.water >= 1 and plant.water <= 10)):
                    if (plant.water < 1):
                        raise WaterError(f"Error: Water level {plant.water}"
                                         f"is too low(min 1) \n")
                    else:
                        raise WaterError(f"Error: Water level {plant.water}"
                                         f"is too high (max 10)\n")
                elif (not (plant.sun >= 2 and plant.sun <= 12)):
                    if (plant.sun < 2):
                        raise GardenError(f"Error: Sunlight hours "
                                          f"{plant.sun} is too low (min 2)\n")
                    else:
                        raise GardenError(f"Error: Sunlight hours {plant.sun}"
                                          f"is too high (max 12)\n")
                else:
                    print(f"{plant.name}: healthy (water: "
                          f"{plant.water}, sun: {plant.sun})")
        except Exception as e:
            print(e)
        finally:
            print("Checking plant health systeme closed")


class Plant:
    """Represents a single plant with a name, water level, and
    sunlight level"""

    def __init__(self, name, water, sun):
        """Initializes a plant with its name, water,
        and sunlight requirements"""
        self.name = name
        self.water = water
        self.sun = sun


def systeme():
    """Runs the garden management system """
    print("=== Garden Management System ===\n")
    p1 = Plant("maticha", 0, 4)
    p2 = Plant("dela7", -10, 12)

    manager = GardenManager(100)
    manager.add(p1)
    manager.add(p2)
    print()
    manager.water_plants()
    print()
    manager.check_health()
    print()

    try:
        print("Testing error recovery...")
        raise GardenError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    finally:
        print("System recovered and continuing...\n")
    print("Garden management system test complete!")


systeme()
