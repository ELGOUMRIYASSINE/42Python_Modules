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
    pass

def memory_vault() -> dict[str, callable]:
    pass

first = mage_counter()
secend = mage_counter()
print(first())
print(first())
