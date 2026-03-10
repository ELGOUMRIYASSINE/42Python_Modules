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
        def wrapper(power: int):
            if power < min_power:
                print(f"Power level too low! Minimum required: {min_power}")
                return
            return func(power)
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

@retry_spell(max_attempts=3)
def spell_connection(api_key: str):
    raise ValueError("Invalid API key!")

result = spell_connection("invalid_key")
