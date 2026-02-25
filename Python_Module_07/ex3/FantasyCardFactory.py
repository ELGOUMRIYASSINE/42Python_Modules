from .CardFactory import CardFactory
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard

class FantasyCardFactory(CardFactory):
    
    def __init__(self):
        # register supported types: dragons, goblins, fireball, mana_ring...
        self.supported_types = {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"]
        }
    
    def create_creature(self, name_or_power) -> Card:
        return CreatureCard(name_or_power, 3, "common", name_or_power, name_or_power)
    
    def create_spell(self, name_or_power) -> Card:
        return SpellCard(name_or_power, cost=2, rarity="uncommon", effect_type="damage")
    
    def create_artifact(self, name_or_power) -> Card:
        return ArtifactCard(name_or_power, cost=4, rarity="rare", durability=5, effect="boost")
    
    def create_themed_deck(self, size: int) -> dict:
        # returns a mixed fantasy deck of given size
        deck = {
            "creatures": [],
            "spells": [],
            "artifacts": []
        }
        for i in range(size):
            if i % 3 == 0:
                deck["creatures"].append(self.create_creature(i))
            elif i % 3 == 1:
                deck["spells"].append(self.create_spell(i))
            else:
                deck["artifacts"].append(self.create_artifact(i))
        return deck
    
    def get_supported_types(self) -> dict:
        return self.supported_types
