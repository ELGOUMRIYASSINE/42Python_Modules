import typing
from abc import ABC, abstractmethod

class Card(ABC):

    def __init__(self, name, cost, rarity):
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict):
        pass

    def get_card_info(self):
        data = {'name': self.name, 'Cost': self.cost, 'Rarity': self.rarity, 'Type': 'Creature'}
        return data

    def is_playable(self, available_mana: int) -> bool:
        return self.cost <= available_mana


    