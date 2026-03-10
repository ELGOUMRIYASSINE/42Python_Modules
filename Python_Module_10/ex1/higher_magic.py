from typing import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    return lambda target: (spell1(target), spell2(target))


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    return lambda: base_spell() * multiplier


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    return lambda target: spell(target) if condition(target) else "freez"


def spell_sequence(spells: list[Callable]) -> Callable:
    return lambda target: [spell(target) for spell in spells]


def test():
    print("---- Testing spell_combiner ----")

    def fireball(target):
        return f"Fireball hits {target}"

    def heal(target):
        return f"Heals {target}"

    combined = spell_combiner(fireball, heal)
    result = combined("Dragon")

    print(result)  
    # Expected: ('Fireball hits Dragon', 'Heals Dragon')


    print("\n---- Testing power_amplifier ----")

    def base_damage():
        return 10

    mega_spell = power_amplifier(base_damage, 3)

    print("Original:", base_damage())
    print("Amplified:", mega_spell())
    # Expected: 30


    print("\n---- Testing conditional_caster ----")

    def is_enemy(target):
        return target == "Dragon"

    fire_spell = conditional_caster(is_enemy, fireball)

    print(fire_spell("Dragon"))   # should cast
    print(fire_spell("Friend"))   # should fail

    print("\n---- Testing spell_sequence ----")

    spells = [fireball, heal]

    sequence = spell_sequence(spells)

    results = sequence("Knight")

    print(results)
    # Expected: ['Fireball hits Knight', 'Heals Knight']


if __name__ == "__main__":
    test()
