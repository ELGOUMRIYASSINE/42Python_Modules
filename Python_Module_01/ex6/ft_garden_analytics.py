class myclassmethod:
    def __init__(self, func):
        self.func = func
        
    def __get__(self, obj, objtype=None):
        def wrapper(*arg, **kwarg):
            return self.func(objtype, *arg, **kwarg)
        return wrapper


class GardenManager:
    """
    Manages multiple gardens and keeps track of statistics.
    This is like a central system that oversees all your gardens.
    """
    total_gardens = 0

    def __init__(self):
        """Creates a new garden manager with an empty list of gardens."""
        self.gardens = []

    def add_garden(self, garden):
        """
        Adds a garden to the manager's list.
        Also increases the total count of gardens being managed.
        """
        self.gardens.append(garden)
        print(f"{garden.name} Added to The Garden Manager Systeme ✔")
        GardenManager.total_gardens += 1

    @myclassmethod
    def get_total_gardens(cls):
        """Shows how many gardens are currently being managed in total."""
        print(f"Total gardens managed: {cls.total_gardens}")
    get_total_gardens = myclassmethod(get_total_gardens)
    @classmethod
    def create_garden_network(cls):
        """
        Creates and returns a new garden management network.
        This is a factory method that sets up a fresh manager instance.
        """
        print("Creating new garden network...")
        return cls()

    def garden_score(self):
        """
        Calculates and displays the score for each garden.
        The score is based on the total height of all plants in the garden.
        """
        rs = ""
        for garden in self.gardens:
            rs += f"{garden.name}: {GardenManager.GardenStats.score(garden)} "
        print(f"Garden scores - {rs}")

    class GardenStats:
        """
        Helper class that provides utility functions
        for calculating garden statistics.
        These methods don't need any specific instance data to work.
        """

        @staticmethod
        def height_validation(garden, min_height):
            """
            Checks if the total height of all plants in a
            garden meets the minimum requirement.
            Prints True if it passes, False if it doesn't.
            """
            total = 0
            state = False
            for plant in garden.plants:
                total += plant.height
            if (total >= min_height):
                state = True
            print(f"Height validation test: {state}")

        @staticmethod
        def score(garden):
            """
            Calculates a garden's score by adding up all plant heights.
            Returns the total score as a number.
            """
            score = 0
            for plant in garden.plants:
                score += plant.height
            return score


class Garden:
    """
    Represents a single garden that can hold multiple plants.
    Each garden has a name and keeps track of its plants.
    """

    def __init__(self, name):
        """Creates a new garden with a given name and an empty plant list."""
        self.name = name
        self.plants = []

    def add_plant(self, plant):
        """Adds a plant to this garden and confirms the addition."""
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.name} garden")

    def get_growth(self, plant):
        """Returns how much a specific plant has grown since it was added."""
        return plant.total_growth()

    def grow_plants(self):
        """
        Makes all plants in the garden grow by 1cm.
        Shows a message for each plant as it grows.
        """
        print(f"{self.name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            print(f"{plant.name} grew {plant.growth}cm")

    def plants_in_garden(self):
        """
        Lists all plants currently in the garden with their details.
        Shows different information depending on the plant type.
        """
        print("Plants in garden:")
        for plant in self.plants:
            if (plant.plant_type == "regular"):
                print(f"- {plant.base_data()}")
            else:
                print(plant.show_data())

    def plants_summary(self):
        """
        Displays a summary of the garden including:
        - Total number of plants
        - Total growth of all plants
        - Count of each plant type
        """
        t_growth = 0
        for plant in self.plants:
            t_growth += plant.total_growth()
        print(f"Plants Added: {self.plants.__len__()}"
              f"Total growth: {t_growth}cm")
        plts = {
            "regular": 0,
            "flowering": 0,
            "prize flowers": 0
        }
        for plant in self.plants:
            if plant.plant_type in plts:
                plts[plant.plant_type] += 1
        print(f"Plant types: {plts['regular']} regular, {plts['flowering']}"
              f"flowering, {plts['prize flowers']} prize flowers ✔")


class Plant:
    """
    Basic plant class that represents any regular plant.
    All other plant types inherit from this base class.
    """
    plant_type = "regular"
    plant_count = 0

    def __init__(self, name, height, age):
        """
        Creates a new plant with a name, starting height, and age.
        Also tracks how much it has grown since creation.
        """
        self.name = name
        self.height = height
        self.age = age
        self.growth = 0
        Plant.plant_count += 1

    def grow(self):
        """Makes the plant grow by 1cm and records the growth."""
        self.height += 1
        self.growth += 1

    def total_growth(self):
        """Returns the total amount this plant
        has grown since it was created."""
        return (self.growth)

    def base_data(self):
        """Returns basic info about the plant: its name and current height."""
        return f"{self.name}: {self.height}"


class FloweringPlant(Plant):
    """
    A plant that produces flowers.
    Inherits all basic plant features and adds flower-specific properties.
    """
    plant_type = "flowering"
    Flower_count = 0

    def __init__(self, name, height, age, color, bloom_status):
        """
        Creates a flowering plant with color and bloom status.
        The bloom status tells us if the plant is currently blooming or not.
        """
        super().__init__(name, height, age)
        self.color = color
        self.bloom_status = bloom_status
        FloweringPlant.Flower_count += 1

    def show_data(self):
        """Returns plant info including
        flower color and whether it's blooming."""
        base_data = self.base_data()
        return f"- {base_data} {self.color} flowers ({self.bloom_status})"


class PrizeFlower(FloweringPlant):
    """
    A special flowering plant that has won prizes.
    This is the most advanced plant type with all
    features of regular and flowering plants,
    plus a prize points system.
    """
    plant_type = "prize flowers"
    PrizeFlower = 0

    def __init__(self, name, height, age, color, bloom_status, prize):
        """
        Creates a prize-winning flower with all flowering
        plant features plusprize points.Prize points indicate
        how valuable or special this plant is.
        """
        super().__init__(name, height, age, color, bloom_status)
        self.prize = prize
        PrizeFlower.PrizeFlower += 1

    def show_data(self):
        """Returns complete plant info including prize points."""
        base_data = self.base_data()
        return (f"- {base_data} {self.color} flowers "
                f"({self.bloom_status}), Prize points: {self.prize}")

print("=== Garden Management System Demo ===")


p1 = Plant("Oak Tree", 20, 19)
p2 = FloweringPlant("Rose", 4, 30, "green", "blooming")
p3 = PrizeFlower("Sunflower", 4, 30, "red", "blooming", 20)
p4 = PrizeFlower("newar chemss", 89, 20, "yellow", "blooming", 20)


g1 = Garden("Alice's")
g2 = Garden("Yassine")

g1.add_plant(p1)
g1.add_plant(p2)
g1.add_plant(p3)
g2.add_plant(p4)

manage = GardenManager.create_garden_network()

manage.add_garden(g1)
manage.add_garden(g2)


print()

g1.grow_plants()

print()

print("=== Alice's Garden Report ===")
g1.plants_in_garden()

print()

g1.plants_summary()

print()

GardenManager.GardenStats.height_validation(g1, 10)
manage.garden_score()
manage.get_total_gardens()
