from abc import ABC, abstractmethod
from ex0.Card import Card
# from ex0.CreatureCard import CreatureCard
# from ex1.SpellCard import SpellCard
# from ex1.ArtifactCard import ArtifactCard
# from ex2.Combatable import Combatable

class CardFactory(ABC):

    @abstractmethod
    def create_creature(self, name_or_power) -> Card:
        # return CreatureCard(name_or_power, cost=3, rarity="common", attack=name_or_power, defense=name_or_power)
        pass

    @abstractmethod
    def create_spell(self, name_or_power) -> Card:
        # return SpellCard(name_or_power, cost=2, rarity="uncommon", effect_type="damage")
        pass

    @abstractmethod
    def create_artifact(self, name_or_power) -> Card:
        # return ArtifactCard(name_or_power, cost=4, rarity="rare", durability=5, effect="boost")
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> dict:
        # return {
        #     "creatures": [self.create_creature(i) for i in range(size//3)],
        #     "spells": [self.create_spell(i) for i in range(size//3)],
        #     "artifacts": [self.create_artifact(i) for i in range(size//3)]
        # }
        pass

    @abstractmethod
    def get_supported_types(self) -> dict:
        # return {
        #     "creatures": ["dragon", "goblin"],
        #     "spells": ["fireball", "heal", "lightning_bolt"],
        #     "artifacts": ["mana_ring", "staff", "crystal"]
        # }
        pass
