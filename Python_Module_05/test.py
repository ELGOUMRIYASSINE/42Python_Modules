from typing import Protocol, runtime_checkable

@runtime_checkable
class CanSpeak(Protocol):
    def speak(self) -> str: ...

class Rock:
    pass

print(isinstance(Rock(), CanSpeak))