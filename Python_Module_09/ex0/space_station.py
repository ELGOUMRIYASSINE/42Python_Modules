from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def main():
    print("========================================")
    try:
        spacestation = SpaceStation(
            station_id="kk120",
            name="test name",
            crew_size=10,
            power_level=89.0,
            oxygen_level=40.0,
            last_maintenance=datetime.now(),
            is_operational=True,
            notes="aaaaaaa"
        )
        print(f"Valid station created: {spacestation.station_id}")
        print(f"ID: {spacestation.station_id}")
        print(f"Name: {spacestation.name}")
        print(f"Crew: {spacestation.crew_size} people")
        print(f"Power: {spacestation.power_level}%")
        print(f"Oxygen: {spacestation.oxygen_level}%")
        print(f"Status: {'Operational' if spacestation.is_operational else 'Not Operational'}\n")  # noqa: E501
    except Exception as e:
        if e.errors()[0]['loc']:
            print(f"{e.errors()[0]['loc'][0]}: {e.errors()[0]['msg']}")
        else:
            print(f"{e.errors()[0]['msg']}")
    print("========================================")
    try:
        spacestation = SpaceStation(
            station_id="kk120",
            name="yassine",
            crew_size=21,
            power_level=89.0,
            oxygen_level=40.0,
            last_maintenance=datetime.now(),
            is_operational=True,
            notes="aaaaaaa"
        )
    except Exception as e:
        print("Expected validation error:")
        if e.errors()[0]['loc']:
            print(f"{e.errors()[0]['loc'][0]}: {e.errors()[0]['msg']}")
        else:
            print(f"{e.errors()[0]['msg']}")


main()
