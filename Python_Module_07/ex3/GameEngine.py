from .CardFactory import CardFactory
from .GameStrategy import GameStrategy
import random

class GameEngine:
    
    def __init__(self):
        self.factory = None
        self.strategy = None
        self.turns_simulated = 0
        self.total_damage = 0
        self.hand = []
    
    def configure_engine(self, factory: CardFactory, strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

        creature_cards = random.randint(1, 5)
        spells_cards = random.randint(1, 4)
        artifacts_cards = 10 - (spells_cards + creature_cards)

        # Example fantasy names
        creature_names = ["Dragon", "Goblin"]
        spell_names = ["Fireball"]
        artifact_names = ["Mana Ring"]

        for _ in range(creature_cards):
            name = random.choice(creature_names)
            self.hand.append(self.factory.create_creature(name))

        for _ in range(spells_cards):
            name = random.choice(spell_names)
            self.hand.append(self.factory.create_spell(name))

        for _ in range(artifacts_cards):
            name = random.choice(artifact_names)
            self.hand.append(self.factory.create_artifact(name))
                
    
    def simulate_turn(self) -> dict:
        battlefield = []
        turn_result = self.strategy.execute_turn(self.hand, battlefield)

        self.turns_simulated += 1
        self.total_damage += turn_result.get("damage_dealt", 0)

        return turn_result
    
    def get_engine_status(self) -> dict:
        # returns turns_simulated, strategy_used, total_damage, cards_created
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": self.strategy.get_strategy_name() if self.strategy else None,
            "total_damage": self.total_damage,
            "cards_created": len(self.hand)
        }