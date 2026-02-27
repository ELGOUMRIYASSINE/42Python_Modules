from ex0.Card import Card


class ArtifactCard(Card):
    card_type = "artifact"

    def __init__(self, name, cost, rarity, durability: int, effect: str):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"Permanent: {self.effect}"
        }

    def activate_ability(self) -> dict:
        return {
            "artifact": self.name,
            "ability": self.effect
        }
