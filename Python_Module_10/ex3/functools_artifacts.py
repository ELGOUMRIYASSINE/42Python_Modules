from functools import reduce, partial, lru_cache, singledispatch
from typing import Callable
import operator
import time


def spell_reducer(spells: list[int], operation: str) -> int:
    operations = {
        "add": operator.add,
        "mul": operator.mul,
        "sub": operator.sub,
        "truediv": operator.truediv
    }
    result = reduce(operations[operation], spells)
    return result


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    enchanters = {
                  'fire_enchant': partial(base_enchantment, power=50),
                  'ice_enchant': partial(base_enchantment, power=50),
                  'lightning_enchant': partial(base_enchantment, power=50)
                }
    return enchanters[base_enchantment.__name__]

@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    @singledispatch
    def handle(value):
        return "No move"

    @handle.register(int)
    def handle_int(value):
        return "dammage spell"

    @handle.register(str)
    def handle_str(value):
        return "healing spell"

    @handle.register(list)
    def handle_float(value):
        return "buff spell"

    return handle



def test_all_functions():

    print("\n---- Testing spell_reducer ----")

    spells = [10, 20, 30]

    print("Add:", spell_reducer(spells, "add"))
    print("Multiply:", spell_reducer(spells, "mul"))
    print("Subtract:", spell_reducer(spells, "sub"))

    print("\n---- Testing partial_enchanter ----")

    def fire_enchant(element: str, target: str, power: int) -> str:
        return f"Enchanted {target} ==> {element} with power {power}"

    def ice_enchant(element: str, target: str, power: int) -> str:
        return f"Enchanted {target} ==> {element} with power {power}"

    def lightning_enchant(element: str, target: str, power: int) -> str:
        return f"Enchanted {target} ==> {element} with power {power}"

    fire = partial_enchanter(fire_enchant)
    ice = partial_enchanter(ice_enchant)
    lightning = partial_enchanter(lightning_enchant)

    print(fire(element="fire", target="sword"))
    print(ice(element="ice", target="shield"))
    print(lightning(element="lightning", target="axe"))

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
    print(dispatcher([10,20,30])) 
    print(dispatcher({})) 


test_all_functions()