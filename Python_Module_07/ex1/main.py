import sys
sys.path.append("/home/yelgoumr/yelgoumr/1337_projects/42Python_Modules/Python_Module_07/ex0")

from Deck import Deck
from ArtifactCard import ArtifactCard
from SpellCard import SpellCard
from CreatureCard import CreatureCard

print("=== DataDeck Deck Builder ===\n")
print("Building deck with different card types...")

card1 = CreatureCard("Fire Dragon", 5, "Rare", 3, 2)
card2 = SpellCard("Lightning Bolt", 3, "Common", "Deal 3 damage to target")
card3 = ArtifactCard("Mana Crystal", 2, "Common", 10, "+1 mana per turn")

deck = Deck()

deck.add_card(card1)
deck.add_card(card2)
deck.add_card(card3)

print("Deck stats:", deck.get_deck_stats())

print("\nDrawing and playing cards:\n")

for _ in range(3):
    card = deck.draw_card()
    print(f"Drew: {card.name} ({card.card_type})")
    result = card.play({"effect": "Creature summoned to battlefield"})
    print(f"Play result: {result}\n")

print("Polymorphism in action: Same interface, different card behaviors!")
