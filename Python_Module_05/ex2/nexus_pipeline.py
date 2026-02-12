from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional, Protocol


# protocol
class ProcessingStage(Protocol):

    def process(self, data: Any) -> Any: ...


class ProcessingPipeline(ABC):
    def __init__(self) -> None:
        self.stages: List[ProcessingStage] = []
        print("Creating Data Processing Pipeline...")

    def add_stage(self, stage: ProcessingStage) -> None:
        pass

    @abstractmethod
    def process(self, data: Any) -> Any:
        pass


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Union[str, Any]:
        pass


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Union[str, Any]:
        pass


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Union[str, Any]:
        pass


class InputStage:
    def process(self, data: Any) -> Any:
        pass


class TransformStage:
    def process(self, data: Any) -> Any:
        pass


class OutputStage:
    def process(self, data: Any) -> Any:
        pass


class NexusManager:
    def __init__(self) -> None:
        self.pipelines: List[ProcessingPipeline] = []
        print("Initializing Nexus Manager...\n\
                Pipeline capacity: 1000 streams/second")

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        pass

    def process_data(self, data: Any) -> Any:
        pass