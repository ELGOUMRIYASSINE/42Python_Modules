from functools import wraps
from typing import Callable
from time import time


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper():
        print(f"Casting {func.__name__}...")
        start_time = time()
        func()
        end_time = time()
        print(f"Spell completed in: {end_time - start_time} seconds")
    return wrapper

def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:

        @wraps(func)
        def wrapper(*args, **kwargs):

            power = args[-1]  # last argument is power

            if power < min_power:
                print(f"Power level too low! Minimum required: {min_power}")
                return

            return func(*args, **kwargs)

        return wrapper

    return decorator


def retry_spell(max_attempts) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(api_key: str):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(api_key)
                except Exception as e:
                    print(f"Spell failed with error: {e}. Retrying... ({attempts + 1}/{max_attempts})")
                    attempts += 1
            print("Max attempts reached. Spell failed.")
        return wrapper
    return decorator

class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """
        Name must:
        - be at least 3 characters
        - contain only letters and spaces
        """

        if len(name) < 3:
            return False

        for char in name:
            if not (char.isalpha() or char == " "):
                return False

        return True


    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with power {power}"


def test_all():

    print("\n----- Testing spell_timer -----")

    @spell_timer
    def slow_spell():
        from time import sleep
        sleep(1)
        print("Spell executed!")

    slow_spell()


    print("\n----- Testing power_validator -----")

    @power_validator(20)
    def power_spell(power):
        return f"Spell cast with power {power}"

    print(power_spell(10))  # should fail
    print(power_spell(25))  # should succeed


    print("\n----- Testing retry_spell -----")

    attempts = {"count": 0}

    @retry_spell(3)
    def unstable_spell(api_key):
        attempts["count"] += 1
        if attempts["count"] < 3:
            raise Exception("Magic interference")
        return f"Spell succeeded using {api_key}"

    print(unstable_spell("MAGIC_KEY"))


    print("\n----- Testing MageGuild staticmethod -----")

    print(MageGuild.validate_mage_name("Merlin"))
    print(MageGuild.validate_mage_name("Al"))
    print(MageGuild.validate_mage_name("Gandalf The Grey"))
    print(MageGuild.validate_mage_name("Mage123"))


    print("\n----- Testing MageGuild.cast_spell (decorator inside class) -----")

    guild = MageGuild()

    print(guild.cast_spell("Fireball", 5))   # should fail
    print(guild.cast_spell("Fireball", 20))  # should succeed

test_all()
