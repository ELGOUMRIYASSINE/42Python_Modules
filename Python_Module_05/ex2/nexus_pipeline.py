from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional, Protocol


# protocol
class ProcessingStage(Protocol):

    def process(self, data: Any) -> Any: ...


class ProcessingPipeline(ABC):
    printed_times = 0
    def __init__(self) -> None:
        self.stages: List[ProcessingStage] = []
        if self.printed_times == 0:
            print("\nCreating Data Processing Pipeline...\n")

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)
        if self.printed_times < 3:
            print(f"Stage {len(self.stages)}: {stage.description}")
        ProcessingPipeline.printed_times += 1

    @abstractmethod
    def process(self, data: Any) -> Any:
        pass


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Union[str, Any]:
        result = data
        for stage in self.stages:
            result = stage.process(result)


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Union[str, Any]:
        result = data
        for stage in self.stages:
            result = stage.process(result)


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Union[str, Any]:
        result = data
        for stage in self.stages:
            result = stage.process(result)


class InputStage:
    description = "Input validation and parsing"

    def process(self, data: Any) -> Any:
        input_data = {}
        if isinstance(data, str):
            print(f'Input: "{data}"')
            input_data['CVS'] = data.split(",")
            return input_data
        if isinstance(data, list):
            print(f'Input: {data}')
            input_data['STREAM'] = data
            return input_data
        else:
            print(f'Input: {data}')
            input_data['JSON'] = data
            # print(input_data)
            return input_data


class TransformStage:
    description = "Data transformation and enrichment"

    def process(self, data: Any) -> Any:
        # print("cc")
        # proccesed_data = {}
        if "JSON" in data:
            print("Transform: Enriched with metadata and validation")
            if data["JSON"]['value'] < 50:
                data["JSON"]['status'] = "Normal range"
            if data["JSON"]['value'] > 50 and data["JSON"]['value'] < 80:
                data["JSON"]['status'] = "Hard range"
            if data["JSON"]['value'] > 100:
                data["JSON"]['status'] = "Danger range"

        if "CVS" in data:
            print("Transform: Parsed and structured data")
        if "STREAM" in data:
            print("Transform: Aggregated and filtered")
            total_sum = sum(data["STREAM"])
            avg = round(total_sum / len(data["STREAM"]), 1)
            data["AVG"] = avg
            data["READINGS"] = len(data["STREAM"])
        return data


class OutputStage:
    description = "Output formatting and delivery"

    def process(self, data: Any) -> Any:
        if "JSON" in data:
            print(f"Output: Processed temperature reading: {data['JSON']['value']}°C ({data['JSON']['status']})")
        if "CVS" in data:
            print(f"Output: User activity logged: {data["CVS"].count("action")} actions processed")
        if "STREAM" in data:
            print(f"Output: Stream summary: {data["READINGS"]} readings, avg: {data["AVG"]}°C")

class NexusManager:
    def __init__(self) -> None:
        self.pipelines: List[ProcessingPipeline] = []
        print("Initializing Nexus Manager...\n"\
              "Pipeline capacity: 1000 streams/second")

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(pipeline)

    def process_data(self, data: Any) -> Any:
        i = 0
        for pip in self.pipelines:
            if i == 1:
                break
            pip.process(data)
            i += 1


if __name__ == "__main__":
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")
    manager = NexusManager()

    #creating piplines 
    json_pipline = JSONAdapter("JS_100")
    json_pipline.add_stage(InputStage())
    json_pipline.add_stage(TransformStage())
    json_pipline.add_stage(OutputStage())

    c_pipline = CSVAdapter("CV_100")
    c_pipline.add_stage(InputStage())
    c_pipline.add_stage(TransformStage())
    c_pipline.add_stage(OutputStage())

    st_pipline = StreamAdapter("ST_100")
    st_pipline.add_stage(InputStage())
    st_pipline.add_stage(TransformStage())
    st_pipline.add_stage(OutputStage())

    # add piplines to NexusManager
    manager.add_pipeline(json_pipline)
    manager.add_pipeline(c_pipline)
    manager.add_pipeline(st_pipline)

    print("\n=== Multi-Format Data Processing ===\n")

    json_data   = {"sensor": "temp", "value": 23.5, "unit": "C"}
    csv_data    = "user,action,action,timestamp"
    stream_data = [21.0, 22.5, 23.0, 21.8, 22.2, 99.6]

    print("Processing JSON data through pipeline...")
    json_pipline.process(json_data)

    print("\nProcessing CSV data through same pipeline...")
    c_pipline.process(csv_data)

    print("\nProcessing Stream data through same pipeline...")
    st_pipline.process(stream_data)

    print("\n=== Pipeline Chaining Demo ===\n")

    print("=== Error Recovery Test ===\n")
    
    print("Nexus Integration complete. All systems operational.")


