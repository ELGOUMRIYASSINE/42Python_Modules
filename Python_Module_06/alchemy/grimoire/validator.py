def validate_ingredients(ingredients: str) -> str:
    valid_elements = ["fire", "water", "earth", "air"]
    for word in valid_elements:
        if word in ingredients:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
