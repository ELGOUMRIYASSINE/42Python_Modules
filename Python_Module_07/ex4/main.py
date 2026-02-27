import random
from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


print("=== DataDeck Tournament Platform ===\n")

print("Registering Tournament Cards...\n")

card1 = TournamentCard("Fire Dragon", 5, "Rare", 3, 2)
card2 = TournamentCard("Ice Wizard", 2, "Common", 5, 1)
platform = TournamentPlatform()

card1.get_rank_info()
card2.get_rank_info()

print("Creating tournament match...\n")

platform.register_card(card1)
platform.register_card(card2)
match_result = platform.create_match("fire_dragon", "ice_wizard")
print(f"Match Result: {match_result}\n")

print("Tournement leaderboard:")
platform.get_leaderboard()

print()

print("platform report:")
report = platform.generate_tournament_report()
print(report)

print("\n=== Tournament Platform Successfully Deployed! ===")
print("All abstract patterns working together harmoniously!")