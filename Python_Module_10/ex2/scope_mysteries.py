from typing import Callable, Any


def mage_counter() -> Callable[[], int]:
    counter: int = 0

    def count_calls() -> int:
        nonlocal counter
        counter += 1
        return counter

    return count_calls


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    power: int = initial_power

    def powers(pwr: int) -> int:
        nonlocal power
        power += pwr
        return power

    return powers


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    return lambda target: f"{enchantment_type} {target}"


def memory_vault() -> dict[str, Callable[..., Any]]:
    memory: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        memory[key] = value

    def recall(key: str) -> Any:
        return memory.get(key, "Memory not found")

    return {"store": store, "recall": recall}


def test() -> None:
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
