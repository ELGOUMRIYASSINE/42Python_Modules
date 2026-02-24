import sys
# sys.path.append("/home/yelgoumr/yelgoumr/1337_projects/42Python_Modules/Python_Module_07/")

print(sys.path)

from ex0.Card import Card
from Combatable import Combatable
from Magical import Magical

class EliteCard(Card, Combatable, Magical):
    def __init__(self, name, cost, attack_power, defense, mana):
        super().__init__(name, cost)
        self.attack_power = attack_power
        self.defense = defense
        self.mana = mana
    def play():
        pass

print("Hello")




