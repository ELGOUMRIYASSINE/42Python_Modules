from functools import reduce, partial, lru_cache, singledispatch
from typing import Callable
import operator
import time


def spell_reducer(spells: list[int], operation: str) -> int:
    """Reduce a list of spell values with the given operation.

    Args:
        spells: A list of integer spell strengths.
        operation: One of 'add', 'mul', 'min', 'max'.

    Returns:
        The integer result of reducing the list with the chosen operation.
    """
    operations = {
        "add": operator.add,
        "mul": operator.mul,
        "min": min,
        "max": max
    }
    result = reduce(operations[operation], spells)
    return result


def partial_enchanter(
    base_enchantment: Callable[..., str],
) -> dict[str, Callable[..., str]]:
    """Create three partial enchantment functions from a base enchantment.

    Args:
        base_enchantment: A function accepting at least `power`,
            `element`, and `target` and returning a string.

    Returns:
        A dict mapping enchantment names to partially-applied
        callables that accept the remaining `target` argument.
    """
    return {
        'fire_enchant': partial(
            base_enchantment,
            power=50,
            element="fire",
        ),
        'ice_enchant': partial(
            base_enchantment,
            power=50,
            element="ice",
        ),
        'lightning_enchant': partial(
            base_enchantment,
            power=50,
            element="lightning",
        ),
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """Return the n-th Fibonacci number using memoization.

    Args:
        n: Index of the Fibonacci sequence (non-negative).

    Returns:
        The n-th Fibonacci number as an integer.
    """
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[object], str]:
    """Create a singledispatch handler that maps types to spell descriptions.

    Returns:
        A callable that accepts a single argument and returns a
        string describing the spell type.
    """
    @singledispatch
    def handle(value: object) -> str:
        return "No move"

    @handle.register(int)
    def handle_int(value: int) -> str:
        return "dammage spell"

    @handle.register(str)
    def handle_str(value: str) -> str:
        return "healing spell"

    @handle.register(list)
    def handle_list(value: list) -> str:
        return "buff spell"

    return handle


def test_all_functions() -> None:
    """Run simple demonstrations for the utilities in this module.

    Prints results for each helper to stdout; intended for manual verification.
    """

    print("\n---- Testing spell_reducer ----")

    spells = [10, 20, 30]

    print("Add:", spell_reducer(spells, "add"))
    print("Multiply:", spell_reducer(spells, "mul"))
    print("min:", spell_reducer(spells, "min"))
    print("max:", spell_reducer(spells, "max"))

    print("\n---- Testing partial_enchanter ----")

    def base_enchantment(power: int, element: str, target: str) -> str:
        return f"Enchanted {target} => {element} with power {power}"

    enchanters = partial_enchanter(base_enchantment)

    print(enchanters['fire_enchant'](target="Sword"))
    print(enchanters['ice_enchant'](target="Shield"))
    print(enchanters['lightning_enchant'](target="Axe"))

    print("\n---- Testing memoized_fibonacci ----")

    start = time.time()
    print("Fib(30):", memoized_fibonacci(30))
    print("First call time:", time.time() - start)

    start = time.time()
    print("Fib(30):", memoized_fibonacci(30))
    print("Second call (cached) time:", time.time() - start)

    print("\n---- Testing spell_dispatcher ----")

    dispatcher = spell_dispatcher()

    print(dispatcher(50))
    print(dispatcher("fire"))
    print(dispatcher([10, 20, 30]))
    print(dispatcher({}))


if __name__ == "__main__":
    test_all_functions()
