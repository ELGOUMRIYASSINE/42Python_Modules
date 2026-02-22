import typing
from Card import Card

class CreatureCard(Card):
    {"x": 10}

    def __init__(self, name, cost, rarity, attack, health):
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health
        self.cost = cost
        self.rarity = rarity

    def play(self):
        {"x": 10}
        x = 10
        print(x)
    

    def get_card_info(self):
        base_info = super().get_card_info()
        return f"{base_info}, Attack: {self.attack}, Health: {self.health}"
    
    def attack_target(self, target):
        pass