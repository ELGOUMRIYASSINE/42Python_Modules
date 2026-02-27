from .GameEngine import GameEngine
from .FantasyCardFactory import FantasyCardFactory
from .AggressiveStrategy import AggressiveStrategy

print("=== DataDeck Game Engine ===")
print()
print("Configuring Fantasy Card Game...")

engine = GameEngine()
factory = FantasyCardFactory()
strategy = AggressiveStrategy()

engine.configure_engine(factory, strategy)

print(f"Factory: {factory.__class__.__name__}")
print(f"Strategy: {strategy.get_strategy_name()}")
print(f"Available types: {factory.get_supported_types()}")

print()

print("Simulating aggressive turn...")

hand_display = ", ".join(f"{card.name} ({card.cost})" for card in engine.hand)
print(f"Hand: [{hand_display}]")

print()

print("Turn execution:")
print(f"Strategy: {strategy.get_strategy_name()}")
turn_result = engine.simulate_turn()
print(f"Actions: {turn_result}")

print()

print("Game Report:")
print(engine.get_engine_status())

print()

print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")