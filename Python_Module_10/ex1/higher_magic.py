from typing import Callable


def spell_combiner(
    spell1: Callable[[str], str],
    spell2: Callable[[str], str],
) -> Callable[[str], tuple[str, str]]:
    return lambda target: (spell1(target), spell2(target))


def power_amplifier(
    base_spell: Callable[[], int],
    multiplier: int,
) -> Callable[[], int]:
    return lambda: base_spell() * multiplier


def conditional_caster(
    condition: Callable[[str], bool],
    spell: Callable[[str], str],
) -> Callable[[str], str]:
    return lambda target: spell(target) if condition(target) else "fizzled"


def spell_sequence(
    spells: list[Callable[[str], str]],
) -> Callable[[str], list[str]]:
    return lambda target: [spell(target) for spell in spells]


def test() -> None:
    print("---- Testing spell_combiner ----")

    def fireball(target: str) -> str:
        return f"Fireball hits {target}"

    def heal(target: str) -> str:
        return f"Heals {target}"

    combined = spell_combiner(fireball, heal)
    result = combined("Dragon")

    print(result)

    print("\n---- Testing power_amplifier ----")

    def base_damage() -> int:
        return 10

    mega_spell = power_amplifier(base_damage, 3)

    print("Original:", base_damage())
    print("Amplified:", mega_spell())

    print("\n---- Testing conditional_caster ----")

    def is_enemy(target: str) -> bool:
        return target == "Dragon"

    fire_spell = conditional_caster(is_enemy, fireball)

    print(fire_spell("Dragon"))
    print(fire_spell("Friend"))

    print("\n---- Testing spell_sequence ----")

    spells = [fireball, heal]

    sequence = spell_sequence(spells)

    results = sequence("Knight")

    print(results)


if __name__ == "__main__":
    test()
