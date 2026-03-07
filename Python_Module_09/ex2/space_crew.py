from pydantic import BaseModel, Field, model_validator
from enum import Enum
from datetime import datetime
from typing import List


class RankEnum(Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: RankEnum
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True

    def __str__(self):
        print(f" -  {self.name} ({self.rank.value}) - {self.specialization}")


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember]
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission(self):
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")
        if (
            RankEnum.commander not in [crew.rank for crew in self.crew] and
            RankEnum.captain not in [crew.rank for crew in self.crew]
           ):
            raise ValueError("Mission must have at least one "
                             "Commander or Captain")
        # check experienced crew (5+ years)
        if self.duration_days > 360:
            experienced_crews = sum(1 for crew_member in self.crew if crew_member.years_experience >= 5)  # noqa: E501
            avg = experienced_crews / len(self.crew)
            # we need 50%
            if avg < 0.5:
                raise ValueError("Missions with duration over 360 "
                                 "days must have at least 50% of"
                                 " the crew with 5+ years of experience")
        for crew_member in self.crew:
            if not crew_member.is_active:
                raise ValueError("All crew members must be active")
        return self


def run():
    print("Space Mission Crew Validation")
    print("=========================================")
    mission1 = SpaceMission(
        mission_id="M0438653",
        mission_name="Deep Space Exploration",
        destination="Proxima Centauri",
        launch_date=datetime(2023, 10, 1),
        duration_days=400,
        crew=[
            CrewMember(
                member_id="C001",
                name="Mehdi",
                rank=RankEnum.commander,
                age=45,
                specialization="Engineering",
                years_experience=12
            ),
            CrewMember(
                member_id="C002",
                name="Brahime",
                rank=RankEnum.officer,
                age=35,
                specialization="Engineering",
                years_experience=11
            ),
            CrewMember(
                member_id="C0023",
                name="Mounire",
                rank=RankEnum.officer,
                age=35,
                specialization="Engineering",
                years_experience=10
            )
        ],
        budget_millions=2500.0
    )

    print("Valid mission created:")
    print(f"Mission: {mission1.mission_name}")
    print(f"Destination: {mission1.destination}")
    print(f"Duration: {mission1.duration_days} days")
    print(f"Budget: ${mission1.budget_millions}M")
    print(f"Crew size: {len(mission1.crew)}")
    print("Crew members:")
    for crew_member in mission1.crew:
        crew_member.__str__()
    print("=========================================")
    print("Expected validation error:")
    try:
        mission1 = SpaceMission(
            mission_id="M0438653",
            mission_name="Deep Space Exploration",
            destination="Proxima Centauri",
            launch_date=datetime(2023, 10, 1),
            duration_days=400,
            crew=[
                CrewMember(
                    member_id="C001",
                    name="Mehdi",
                    rank=RankEnum.officer,
                    age=45,
                    specialization="Engineering",
                    years_experience=12
                ),
                CrewMember(
                    member_id="C002",
                    name="Brahime",
                    rank=RankEnum.officer,
                    age=35,
                    specialization="Engineering",
                    years_experience=10
                ),
                CrewMember(
                    member_id="C0023",
                    name="Mounire",
                    rank=RankEnum.officer,
                    age=35,
                    specialization="Engineering",
                    years_experience=10
                )
            ],
            budget_millions=2500.0
        )
    except Exception as e:
        print(e.errors()[0]['msg'])


run()
