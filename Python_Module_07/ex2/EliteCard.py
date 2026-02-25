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

    def play(self):
        pass
    
    def attack(self, target):
        return {
            "damage": self.attack_power,
            "target": target.name,
            "attacker": self.name,
            "combat_type": "melee"
        }

    def defend(self, incoming_damage):
        damage_after_defense = max(0, incoming_damage - self.defense)
        return {
            "damage_taken": damage_after_defense,
            "defender": self.name,
            "remaining_defense": self.defense - incoming_damage,
            "still_alive": damage_after_defense < self.defense
        }
    
print("Hello")




