from .CardFactory import CardFactory
from .GameStrategy import GameStrategy

class GameEngine:
    
    def __init__(self):
        self.factory = None
        self.strategy = None
        self.turns_simulated = 0
        self.total_damage = 0
        self.hand = []
    
    def configure_engine(self, factory: CardFactory, strategy: GameStrategy) -> None:
        # sets factory and strategy
        self.factory = factory
        self.strategy = strategy
        # generates initial hand using factory
        self.hand = [self.factory.create_creature("Creature")] * 5
    
    def simulate_turn(self) -> dict:
        battlefield = []  # This would be populated with actual game state in a real implementation
        turn_result = self.strategy.execute_turn(self.hand, battlefield)
        self.turns_simulated += 1
        self.total_damage += sum(action.get("damage_dealt", 0) for action in turn_result.get("targets_prioritized", []))
        return turn_result
    
    def get_engine_status(self) -> dict:
        # returns turns_simulated, strategy_used, total_damage, cards_created
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": self.strategy.get_strategy_name() if self.strategy else None,
            "total_damage": self.total_damage,
            "cards_created": len(self.hand)
        }