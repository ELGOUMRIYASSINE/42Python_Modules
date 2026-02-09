from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    """Abstract base class for data processors"""

    @abstractmethod
    def process(self, data: Any) -> str:
        """Process the data and return result string"""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate if data is appropriate for this processor"""
        pass

    def format_output(self, result: str) -> str:
        """Default formatting - can be overridden in subclasses"""
        pass


class NumericProcessor(DataProcessor):
    """Processor for numeric data"""

    def process(self, data: Any) -> str:
        """Process numeric data"""
        pass

    def validate(self, data: Any) -> bool:
        """Validate numeric data"""
        for value in data:
            if not isinstance(value, int):
                return False
        return True
                

    def format_output(self, result: str) -> str:
        """Format numeric output"""
        pass


class TextProcessor(DataProcessor):
    """Processor for text data"""

    def process(self, data: Any) -> str:
        """Process text data"""
        pass

    def validate(self, data: Any) -> bool:
        """Validate text data"""
        if not isinstance(data, str) or not data:
            return False
        return True

    def format_output(self, result: str) -> str:
        """Format text output"""
        pass


class LogProcessor(DataProcessor):
    """Processor for log data"""

    def process(self, data: Any) -> str:
        """Process log data"""
        pass

    def validate(self, data: Any) -> bool:
        """Validate log data"""
        if not isinstance(data, str):
            return False
        if not "[" in data or not "]" in data:
            return False
        return True

    def format_output(self, result: str) -> str:
        """Format log output"""
        pass


def process_data(processor: DataProcessor, data: Any) -> None:
    """Polymorphic function that works with any DataProcessor"""
    if processor.validate():


# Main execution
if __name__ == "__main__":
    pass