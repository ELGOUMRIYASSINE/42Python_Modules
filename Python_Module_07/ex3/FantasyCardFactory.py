from .CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class FantasyCardFactory(CardFactory):

    def __init__(self):
        self.supported_types = {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"]
        }
        # Template data provides deterministic stats for each supported type.
        self.creature_templates = {
            "dragon": {
                "name": "Fire Dragon",
                "cost": 5,
                "rarity": "mythic",
                "attack": 5,
                "defense": 4
            },
            "goblin": {
                "name": "Goblin Warrior",
                "cost": 2,
                "rarity": "common",
                "attack": 5,
                "defense": 1
            }
        }
        self.spell_templates = {
            "fireball": {
                "name": "Lightning Bolt",
                "cost": 3,
                "rarity": "uncommon",
                "effect_type": "damage",
                "damage": 3
            }
        }
        self.artifact_templates = {
            "mana_ring": {
                "name": "Mana Ring",
                "cost": 4,
                "rarity": "rare",
                "durability": 5,
                "effect": "boost"
            }
        }

    def _resolve_template(self, templates: dict, card_type: str) -> dict:
        try:
            return templates[card_type.lower()]
        except KeyError as exc:
            raise ValueError(f"Unsupported card type '{card_type}'.") from exc

    def create_creature(self, name_or_power) -> CreatureCard:
        data = self._resolve_template(self.creature_templates, name_or_power)
        return CreatureCard(
            data["name"],
            data["cost"],
            data["rarity"],
            data["attack"],
            data["defense"]
        )

    def create_spell(self, name_or_power) -> SpellCard:
        data = self._resolve_template(self.spell_templates, name_or_power)
        spell = SpellCard(
            data["name"],
            cost=data["cost"],
            rarity=data["rarity"],
            effect_type=data["effect_type"]
        )
        spell.damage = data["damage"]
        return spell

    def create_artifact(self, name_or_power) -> ArtifactCard:
        data = self._resolve_template(self.artifact_templates, name_or_power)
        return ArtifactCard(
            data["name"],
            cost=data["cost"],
            rarity=data["rarity"],
            durability=data["durability"],
            effect=data["effect"]
        )

    def create_themed_deck(self, size: int) -> dict:
        deck = {"creatures": [], "spells": [], "artifacts": []}
        sequence = [
            ("creatures", self.create_creature, "dragon"),
            ("creatures", self.create_creature, "goblin"),
            ("spells", self.create_spell, "fireball"),
            ("artifacts", self.create_artifact, "mana_ring")
        ]
        for idx in range(size):
            category, builder, template_key = sequence[idx % len(sequence)]
            deck[category].append(builder(template_key))
        return deck

    def get_supported_types(self) -> dict:
        return self.supported_types
