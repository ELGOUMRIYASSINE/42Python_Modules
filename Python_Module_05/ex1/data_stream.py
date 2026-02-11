from abc import ABC, abstractmethod
from typing import Any, List, Optional, Union, Dict


class DataStream(ABC):

    def __init__(self, stream_id):
        self.stream_id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    # criteria will have two values check or ignore !"if check i will just
    # check if the data does no have error or not empty"
    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria == "check":
            for data in data_batch:
                if "ERROR" in data:
                    data_batch.remove(data)
        if not data_batch:
            raise ValueError("Alert: No Data Provided")
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        pass


class SensorStream(DataStream):
    def __init__(self, stream_id):
        super().__init__(stream_id)
        self.stream_type = "Environmental Data"
        self.total_readings = 0
        self.temperature_sum = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        result = f"{len(data_batch)} readings processed"
        for value in data_batch:
            if "temp" in value:
                result += f", avg temp: {value.split(':')[1]}"
        self.total_readings = len(data_batch)
        return result

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "stream_type": self.stream_type,
            "total_readings": self.total_readings,
        }


class TransactionStream(DataStream):
    def __init__(self, stream_id):
        super().__init__(stream_id)
        self.stream_type = "Financial Data"
        self.total_operations = 0
        self.buy_count = 0
        self.sell_count = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        total_buys = 0
        index = 0
        i = 0
        for value in data_batch:
            if "buy" in value:
                self.buy_count += 1
            if "sell" in value:
                index = i
            i += 1
        net_flow = total_buys - int(data_batch[index].split(":")[1])
        self.total_operations = len(data_batch)
        self.buy_count = total_buys
        self.sell_count = int(data_batch[index].split(":")[1])
        return (f"{len(data_batch)} operations,  net flow: {net_flow}")

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "stream_type": self.stream_type,
            "total_operations": self.total_operations,
            "buy_count": self.buy_count,
            "sell_count": self.sell_count
        }


class EventStream(DataStream):
    def __init__(self, stream_id):
        super().__init__(stream_id)
        self.stream_type = "System Events"
        self.total_events = 0
        self.errors_detected = 0
        self.login_count = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        self.total_events = len(data_batch)
        counter = 0
        for value in data_batch:
            if value == "error":
                counter += 1
            if value == "login":
                self.login_count += 1
        self.errors_detected = counter
        return (f"{len(data_batch)} events,  error detected: {counter}")

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "stream_type": self.stream_type,
            "total_events": self.total_events,
            "errors": self.errors_detected,
            "logins": self.login_count
        }


class StreamProcessor:
    def __init__(self):
        self.streams = []

    def add_stream(self, stream: DataStream):
        self.streams.append(stream)

    def process_all(
        self,
        data_dict: Dict[str, List[Any]]
    ) -> Dict[str, str]:
        results = {}

        for stream in self.streams:
            if (isinstance(stream, SensorStream)
                    and "sensor" in data_dict):
                result = stream.process_batch(data_dict["sensor"])
                results["sensor"] = result

            elif (isinstance(stream, TransactionStream)
                    and "transaction" in data_dict):
                result = stream.process_batch(data_dict["transaction"])
                results["transaction"] = result

            elif (isinstance(stream, EventStream)
                    and "event" in data_dict):
                result = stream.process_batch(data_dict["event"])
                results["event"] = result

        return results

    def get_all_stats(self) -> List[Dict[str, Union[str, int, float]]]:
        all_stats = []
        for stream in self.streams:
            stats = stream.get_stats()
            all_stats.append(stats)
        return all_stats


if __name__ == "__main__":

    # data to test
    sensor_batch_1 = ["temp:22.5", "humidity:65", "pressure:1013"]
    transaction_batch_1 = ["buy:100", "sell:150", "buy:75"]
    event_batch_1 = ["login", "error", "logout"]

    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")
    s_stream = SensorStream("S1_10")
    print("Initializing Sensor Stream...")
    print(f"Stream ID: {s_stream.stream_id}, Type: {s_stream.stream_type}")
    print(f"Processing sensor batch: {sensor_batch_1}")
    filtred_data = s_stream.filter_data(sensor_batch_1)
    result = s_stream.process_batch(filtred_data)
    print(f"Sensor analysis: {result}")

    s_stream = TransactionStream("T2_11")
    print("\nInitializing Transaction Stream...")
    print(f"Stream ID: {s_stream.stream_id}, Type: {s_stream.stream_type}")
    print(f"Processing transaction batch: {transaction_batch_1}")
    filtred_data = s_stream.filter_data(transaction_batch_1)
    result = s_stream.process_batch(filtred_data)
    print(f"Transaction analysis: {result}")

    s_stream = EventStream("E1_11")
    print("\nInitializing Event Stream...")
    print(f"Stream ID: {s_stream.stream_id}, Type: {s_stream.stream_type}")
    print(f"Processing event batch: {event_batch_1}")
    filtred_data = s_stream.filter_data(event_batch_1)
    result = s_stream.process_batch(filtred_data)
    print(f"Event analysis: {result}")

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")
    print("Batch 1 Results:")
    processor = StreamProcessor()

    processor.add_stream(SensorStream("SEN_001"))
    processor.add_stream(TransactionStream("TRA_001"))
    processor.add_stream(EventStream("EVE_001"))

    mixed_data = {
        "sensor": ["temp:21.0", "humidity:70"],
        "transaction": ["buy:500", "sell:300", "buy:200"],
        "event": ["login", "error", "logout"]
    }

    results = processor.process_all(mixed_data)
    print(f"- Sensor data: {results.get('sensor', 'None')}")
    print(f"- Transaction data: {results.get('transaction', 'None')}")
    print(f"- Event data: {results.get('event', 'None')}")

    print("\n=== Stream Statistics ===\n")
    all_stats = processor.get_all_stats()
    for stats in all_stats:
        print(f"Stream {stats['stream_id']}: {stats}")

    print("\nAll streams processed successfully. Nexus throughput optimal.")
