import sys
sys.path.append("/home/yelgoumr/yelgoumr/1337_projects/42Python_Modules/Python_Module_07/ex0")

from Card import Card

class SpellCard(Card):
    card_type = "spell"
    def __init__(self, name, cost, rarity, effect_type):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect_type
        }

    def resolve_effect(self, targets: list) -> dict:
        return {
            "effect_type": self.effect_type,
            "targets": targets
        }

