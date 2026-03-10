mages = [
    {"name": "Aelric", "power": 120, "type": "fire"},
    {"name": "Lyra", "power": 95, "type": "ice"},
    {"name": "Thalion", "power": 150, "type": "arcane"},
    {"name": "Seraphina", "power": 110, "type": "lightning"},
    {"name": "Darius", "power": 80, "type": "shadow"},
    {"name": "Elowen", "power": 70, "type": "nature"},
    {"name": "Kael", "power": 130, "type": "fire"}
]

spells = [
    "fireball",
    "teleport",
    "invisibility"
]


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(
        artifacts,
        key=lambda artifacts: artifacts["power"],
        reverse=True,
    )


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: "* " + spell + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    result = {"max_power": None, "min_power": None, "avg_power": None}
    result["max_power"] = max(map(lambda mage: mage['power'], mages))
    result["min_power"] = min(map(lambda mage: mage['power'], mages))
    result["avg_power"] = (
        sum(map(lambda mage: mage['power'], mages)) / len(mages)
    )

    return result


print("Testing artifact sorter...")
print(artifact_sorter(mages))
print("")
print("Testing power filter...")
print(power_filter(mages, 100))
print("")
print("Testing spell transformer...")
print(spell_transformer(spells))
print("")
print("Testing mage stats...")
print(mage_stats(mages))
