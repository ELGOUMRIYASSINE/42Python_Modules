def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients
    validation_result = validate_ingredients(ingredients)
    if "- VALID" in validation_result:
        return f"Spell recorded: {spell_name} ({validation_result})"
    return f"Spell rejected: {spell_name} ({validation_result})"

def record_spell_di(spell_name: str, ingredients: str, validator):
    validation_result = validator(ingredients)
    if "- VALID" in validation_result:
        return f"Spell recorded: {spell_name} ({validation_result})"
    return f"Spell rejected: {spell_name} ({validation_result})"
