#!/usr/bin/python3
class Plant:
    # create class attribute that will be shared between all objects to count number of Plants
    Plants = 0
    def __init__(self, name, Height, Age):
        Plant.Plants += 1
        self.name = name
        self.Height = Height
        self.Age = Age
    def display_data(self):
        print(f"Created: {self.name.capitalize()} ({self.Height}cm, {self.Age} days)")

Plant1 = Plant("Rose", 25, 30)
Plant2 = Plant("Broccoli", 21, 12)
Plant3 = Plant("Carrot", 54, 23)
Plant4 = Plant("Potato", 11, 19)
Plant5 = Plant("Spinach", 33, 22)

print("=== Plant Factory Output ===")
Plant1.display_data()
Plant2.display_data()
Plant3.display_data()
Plant4.display_data()
Plant5.display_data()
print(f"Total plants created: {Plant.Plants}")