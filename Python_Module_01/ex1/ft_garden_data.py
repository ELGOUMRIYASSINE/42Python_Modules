#!/usr/bin/python3
class Plant:
    def __init__(self, name, Height, Age):
        self.name = name
        self.Height = f"{Height}cm"
        self.Age = f"{Age} days old"

    def show_plant_data(self):
        print(f"{self.name}: {self.Height}, {self.Age}")


print("=== Garden Plant Registry ===")
pl1 = Plant("Rose", 7, 20)
pl2 = Plant("tomate", 4, 32)
pl3 = Plant("Sunflower", 12, 17)
pl1.show_plant_data()
pl2.show_plant_data()
pl3.show_plant_data()
