from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output : {result}"


class NumericProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        length = 0
        avg = 0
        sum = 0
        if isinstance(data, int):
            length = 1
            sum = data
            avg = sum / length
        else:
            for nb in data:
                length += 1
                sum += nb
            avg = sum / length
        return (f"Processed {length} numeric values, sum={sum},"
                f" avg={avg:.1f}")

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        else:
            for value in data:
                if not isinstance(value, (int, float)):
                    return False
        return True


class TextProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        length = data.__len__()
        words = data.split().__len__()
        return f"Processed text: {length} characters, {words} words"

    def validate(self, data: Any) -> bool:
        if not isinstance(data, str) or not data:
            return False
        return True


class LogProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        if "ERROR" in data:
            return f"[ALERT] ERROR level detected:{data.split(':')[1]}"
        if "INFO" in data:
            return f"[INFO] INFO level detected:{data.split(':')[1]}"

    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            return False
        if "ERROR" not in data and "INFO" not in data:
            return False
        if ":" not in data:
            return False
        return True


def process_data(processor: DataProcessor, data: Any) -> None:
    """Polymorphic function that works with any DataProcessor"""
    print(f"Processing data: {data}")
    try:
        if processor.validate(data):
            if isinstance(processor, NumericProcessor):
                print("Validation: Numeric data verified")
            if isinstance(processor, TextProcessor):
                print("Validation: Text data verified")
            if isinstance(processor, LogProcessor):
                print("Validation: Log entry verified")
            result = processor.process(data)
            print(processor.format_output(result))
        else:
            print("Error: Invalid Data")
    except Exception as e:
        print(f"Error: somthing wrong {e}")


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    print("Initializing Numeric Processor...")
    process_data(NumericProcessor(), 4)

    print()
    print("Initializing Text Processor...")
    process_data(TextProcessor(), "Hello Nexus World")

    print()
    print("Initializing Log Processor...")
    process_data(LogProcessor(), "ERROR: Connection timeout")

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    processes = [NumericProcessor(), TextProcessor(), LogProcessor()]
    data = [4, "My name is yassine", "INFO: System ready"]
    i = 0
    for process in processes:
        if process.validate(data[i]):
            print(f"Result {i + 1}: {process.process(data[i])}")
        else:
            print(f"Error: Invalide Data => {data[i]}")
        i += 1
    print("\nFoundation systems online. Nexus ready for advanced streams.")
