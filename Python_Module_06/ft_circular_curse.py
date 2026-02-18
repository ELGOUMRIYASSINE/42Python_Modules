import alchemy.grimoire
from alchemy.grimoire.validator import validate_ingredients

print("=== Circular Curse Breaking ===\n")

print("Testing ingredient validation:")
print(f'validate_ingredients("fire air"): {alchemy.grimoire.validate_ingredients("fire air")}')
print(f'validate_ingredients("dragon scales"): {alchemy.grimoire.validate_ingredients("dragon scales")}\n')

print("Testing spell recording with validation:")
print(f'record_spell("Fireball", "fire air"): {alchemy.grimoire.record_spell("Fireball", "fire air")}')
print(f'record_spell("Dark Magic", "shadow"): {alchemy.grimoire.record_spell("Dark Magic", "shadow")}\n')

print("Testing late import technique:")

from alchemy.grimoire.spellbook import record_spell
print(f'record_spell("Lightning", "air"): {record_spell("Lightning", "air")}\n')

print("\nTesting dependency injection technique:")
print(f'record_spell_di("Fireball", "fire"): {alchemy.grimoire.record_spell_di("Fireball", "fire", validate_ingredients)}')
print(f'record_spell_di("Dark Magic", "shadow"): {alchemy.grimoire.record_spell_di("Dark Magic", "shadow", validate_ingredients)}\n')

print("Circular dependency curse avoided using late imports!")
print("All spells processed safely!")
