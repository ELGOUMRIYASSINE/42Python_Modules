def mage_counter() -> callable:
    counter = 0

    def count_calls():
        nonlocal counter
        counter += 1
        return counter
    return count_calls


def spell_accumulator(initial_power: int) -> callable:
    power = initial_power

    def powers(pwr):
        nonlocal power
        power += pwr
        return power
    return powers


def enchantment_factory(enchantment_type: str) -> callable:
    return lambda target: f"{enchantment_type} {target}"


def memory_vault() -> dict[str, callable]:
    memory = {}

    def store(key, value):
        memory[key] = value

    def recall(key):
        return memory.get(key, "Memory not found")
    return {"store": store, "recall": recall}


def test():
    print("---- Testing mage_counter ----")
    counter = mage_counter()

    print(counter())
    print(counter())
    print(counter())


    print("\n---- Testing spell_accumulator ----")
    accumulator = spell_accumulator(10)

    print(accumulator(5))
    print(accumulator(10))
    print(accumulator(3))


    print("\n---- Testing enchantment_factory ----")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")

    print(flaming("Sword"))
    print(frozen("Shield"))


    print("\n---- Testing memory_vault ----")
    vault = memory_vault()

    vault["store"]("mage", "Gandalf")
    vault["store"]("artifact", "Magic Staff")

    print(vault["recall"]("mage"))
    print(vault["recall"]("artifact"))
    print(vault["recall"]("dragon"))


if __name__ == "__main__":
    test()
