from .CardFactory import CardFactory
from .GameStrategy import GameStrategy


class EnemyTarget:
    """Simple battlefield target so strategies can prioritize attacks."""

    def __init__(self, name: str, defense: int):
        self.name = name
        self._defense = defense

    def get_combat_stats(self) -> dict:
        return {"defense": self._defense}


class GameEngine:

    def __init__(self):
        self.factory = None
        self.strategy = None
        self.turns_simulated = 0
        self.total_damage = 0
        self.hand = []
        self.battlefield_targets = []

    def configure_engine(
        self,
        factory: CardFactory,
        strategy: GameStrategy
    ) -> None:

        self.factory = factory
        self.strategy = strategy
        self.turns_simulated = 0
        self.total_damage = 0

        self.hand = [
            self.factory.create_creature("dragon"),
            self.factory.create_creature("goblin"),
            self.factory.create_spell("fireball")
        ]
        self.battlefield_targets = [EnemyTarget("Enemy Player", defense=1)]

    def simulate_turn(self) -> dict:
        battlefield = list(self.battlefield_targets)
        turn_result = self.strategy.execute_turn(self.hand, battlefield)

        self.turns_simulated += 1
        self.total_damage += turn_result.get("damage_dealt", 0)

        return turn_result

    def get_engine_status(self) -> dict:
        st_used = self.strategy.get_strategy_name() if self.strategy else None
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": st_used,
            "total_damage": self.total_damage,
            "cards_created": len(self.hand)
        }
