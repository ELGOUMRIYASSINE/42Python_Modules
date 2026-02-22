import sys
from CreatureCard import CreatureCard

# print(sys.path)

print("=== DataDeck Card Foundation ===\n")

print("Testing Abstract Base Class Design:\n")

creature_card = CreatureCard("Goblin", 2, "Common", 3, 2)
print(creature_card.get_card_info())