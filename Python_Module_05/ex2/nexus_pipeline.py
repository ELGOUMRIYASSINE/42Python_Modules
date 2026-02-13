from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional, Protocol


# protocol
class ProcessingStage(Protocol):

    def process(self, data: Any) -> Any: ...


class ProcessingPipeline(ABC):
    def __init__(self) -> None:
        self.stages: List[ProcessingStage] = []
        print("\nCreating Data Processing Pipeline...\n")

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)
        print(f"Stage {len(self.stages)}: {stage.description}")

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
    description = "Input validation and parsing"

    def process(self, data: Any) -> Any:
        input_data = {}
        if "," in data:
            print(f'Input: "{data}"')
            input_data['CVS'] = data.split(",")
            return input_data
        if isinstance(data, dict):
            print(f'Input: {data}')
            input_data['STREAM'] = data.split(",")
            return input_data
        else:
            print(f'Input: {data}')
            input_data['JSON'] = data.split(",")
            return input_data



class TransformStage:
    description = "Data transformation and enrichment"

    def process(self, data: Any) -> Any:
        # proccesed_data = {}
        if "JSON" in data:
            print("Transform: Enriched with metadata and validation")
            if data["JSON"]['value'] < 50:
                data["JSON"]['status'] = "Normal range"
            if data["JSON"]['value'] > 50 and data['value'] < 80:
                data["JSON"]['status'] = "Hard range"
            if data["JSON"]['value'] > 100:
                data["JSON"]['status'] = "Danger range"
            
        if "CVS" in data:
            pass
        if "STREAM" in data:
            pass 
        return data


class OutputStage:
    description = "Output formatting and delivery"

    def process(self, data: Any) -> Any:
        print(f"Output: Processed temperature reading: {data['value']}°C ({data['status']})")


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
            pip.stages[i].process(data)
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
    
    manager.process_data({"sensor": "temp", "value": 23.5, "unit": "C"})
    manager.process_data("user,action,timestamp")
    # manager.process_data({"sensor": "temp", "value": 23.5, "unit": "C"})
    # manager.process_data({"sensor": "temp", "value": 23.5, "unit": "C"})

    
