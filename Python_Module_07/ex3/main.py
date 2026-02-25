from .GameEngine import GameEngine
from .CardFactory import CardFactory
from .FantasyCardFactory import FantasyCardFactory
from .GameStrategy import GameStrategy
from .AggressiveStrategy import AggressiveStrategy

# if __name__ == "__main__":
#     factory

print("=== DataDeck Game Engine ===\n")

print("Configuring Fantasy Card Game...")

engine = GameEngine()
factory = FantasyCardFactory()
strategy = AggressiveStrategy()
engine.configure_engine(factory, strategy)

print("factory:", factory.__class__.__name__)
print("strategy:", strategy.get_strategy_name())
print("Available types:", factory.get_supported_types())

print()

print("simulating aggressive turns...")
print("Hand:", [card.name for card in engine.hand])

print("Turn execution:")
print("Strategy:", strategy.__class__.__name__)
print("Action:", strategy.execute_turn(engine.hand, []))
