from .GameEngine import GameEngine
from .FantasyCardFactory import FantasyCardFactory
from .AggressiveStrategy import AggressiveStrategy

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
print("Simulating aggressive turn...")
print("Hand:", [card.name for card in engine.hand])

print()
print("Turn execution:")
turn_result = engine.simulate_turn()
print('actions', turn_result)

print()
print("Game Report:", engine.get_engine_status())
print()

print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")