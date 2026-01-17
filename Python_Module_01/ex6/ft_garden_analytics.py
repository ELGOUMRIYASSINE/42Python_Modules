class GardenManager:
    pass

class Garden:
    def __init__(self, name):
        self.name = name
        self.plants = []
    def add_plant(self,plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.name} garden")
    def get_growth(self,plant):
        return plant.total_growth()
    def grow_plants(self):
        print(f"{self.name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            print(f"{plant.name} grew {plant.growth}cm")
    def plants_in_garden(self):
        print("Plants in garden:")
        for plant in self.plants:
            if (plant.plant_type == "regular"):
                print(f"- {plant.base_data()}")
                # print(plant.plant_type)
            else:
                print(plant.show_data())
                # print(plant.plant_type)
    def plants_summary(self):
        t_growth = 0
        for plant in self.plants:
            t_growth += plant.total_growth()
        print(f"Plants Added: {self.plants.__len__()} Total growth: {t_growth}cm")
        plants = {
            "regular": 0,
            "flowering": 0,
            "prize flowers": 0
        }
        for plant in self.plants:
            if plant.plant_type in plants:
                plants[plant.plant_type] += 1
        print(f"Plant types: {plants["regular"]} regular, {plants["flowering"]} flowering, {plants["prize flowers"]} prize flowers")

    
class Plant:
    plant_type = "regular"
    plant_count = 0
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        self.growth = 0
        Plant.plant_count += 1
    def grow(self):
        self.height += 1
        self.growth += 1
    def total_growth(self):
        return (self.growth)
    def base_data(self):
        return f"{self.name}: {self.height}"
        
class FloweringPlant(Plant):
    plant_type = "flowering"
    Flower_count = 0
    def __init__(self, name, height, age, color, bloom_status):
        super().__init__(name, height, age)
        self.color = color
        self.bloom_status = bloom_status
        FloweringPlant.Flower_count += 1
    def show_data(self):
        base_data = self.base_data()
        return f"- {base_data} {self.color} flowers ({self.bloom_status})"

class PrizeFlower(FloweringPlant):
    plant_type = "prize flowers"
    PrizeFlower = 0
    def __init__(self, name, height, age, color, bloom_status, prize):
        super().__init__(name, height, age, color, bloom_status)
        self.prize = prize
        PrizeFlower.PrizeFlower += 1
    def show_data(self):
        base_data = self.base_data()
        return f"- {base_data} {self.color} flowers ({self.bloom_status}), Prize points: {self.prize}"

        
print("=== Garden Management System Demo ===")


p1 = Plant("Oak Tree", 20, 19)
p2 = FloweringPlant("Rose", 4, 30, "green", "blooming")
p3 = PrizeFlower("Sunflower", 4, 30, "red", "blooming", 20)


g1 = Garden("Alice's")
g1.add_plant(p1)
g1.add_plant(p2)
g1.add_plant(p3)


print()

g1.grow_plants()

print()

print("=== Alice's Garden Report ===")
g1.plants_in_garden()

print()

g1.plants_summary()
