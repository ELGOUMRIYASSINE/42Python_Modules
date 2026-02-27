from ex0.Card import Card
from .Combatable import Combatable
from .Magical import Magical

class EliteCard(Card, Combatable, Magical):
    def __init__(self, name, cost, attack_power, defense, mana, rarity):
        super().__init__(name, cost, rarity)
        self.attack_power = attack_power
        self.defense = defense
        self.mana = mana

    def play(self):
        return f"{self.name} has been played with attack power {self.attack_power} and defense {self.defense}."

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
            "defender": self.name,
            "damage_taken": damage_after_defense,
            "damage_blocked": min(self.defense, incoming_damage),
            "still_alive": damage_after_defense < self.defense
        }

    def get_combat_stats(self):
        return {
            "attack_power": self.attack_power,
            "defense": self.defense
        }

    def cast_spell(self, spell_name, targets):
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": [target.name for target in targets],
            "mana_cost": 10
        }

    def channel_mana(self, amount):
        self.mana += amount
        return {
            "channeled": amount,
            "total_mana": self.mana,
        }

    def get_magic_stats(self):
        return {
            "mana": self.mana
        }
