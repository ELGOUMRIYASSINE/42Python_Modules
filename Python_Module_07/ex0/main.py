from .CreatureCard import CreatureCard

print("=== DataDeck Card Foundation ===\n")

print("Testing Abstract Base Class Design:\n")

fire_dragon = CreatureCard("Fire Dragon", 2, "Common", 3, 2)
goblin_warrior = CreatureCard("Goblin Warrior", 9, "Common", 3, 10)

print("CreatureCard Info:")
print(fire_dragon.get_card_info())
print("\nPlaying Fire Dragon with 6 mana available:")
print(f"Playable: {fire_dragon.is_playable(6)}")
print(f"Play Result: {fire_dragon.play({'effect': 'Creature summoned to battlefield'})}\n")
print("Fire Dragon attacks Goblin Warrior:")

print("Abstract pattern successfully demonstrated!")
print(f"Attack result: {fire_dragon.attack_target(goblin_warrior)}\n")

print(f"Testing insufficient mana (1 available):")
print(f"Playable: {fire_dragon.is_playable(1)}\n")

print("Abstract pattern successfully demonstrated!")

