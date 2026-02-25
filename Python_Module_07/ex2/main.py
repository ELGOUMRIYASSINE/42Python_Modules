from .EliteCard import EliteCard


elitecard = EliteCard("Arcane Warrior", 5, 7, 3, 20, "Legendary")
enemy = EliteCard("Enemy", 4, 3, 4, 15, "Normal")

print("=== DataDeck Ability System ===\n")

print("EliteCard capabilities:")
print("  - Card: ['play', 'get_card_info', 'is_playable']")
print("  - Combatable: ['attack', 'defend', 'get_combat_stats']")
print("  - Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']\n")

print("Playing Arcane Warrior (Elite Card):\n")

print("Combat phase:")

print(f"Attack result: {elitecard.attack(enemy)}")
print(f"Defense result: {elitecard.defend(7)}\n")

print("Magic phase:")

print(f"Spell cast: {elitecard.cast_spell('Fireball', [enemy])}")
print(f"Mana channel: {elitecard.channel_mana(5)}\n")

print("Multiple interface implementation successful!")
