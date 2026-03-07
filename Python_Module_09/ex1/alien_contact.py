from enum import Enum
from datetime import datetime
from pydantic import BaseModel, Field, model_validator
from typing import list


class ContactType(Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str = Field(max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def custom_validator(self):
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")
        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contacts must be verified")
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("High signal strength requires a received message")
        if self.contact_type == ContactType.telepathic and self.witness_count < 3:
            raise ValueError("Telepathic contacts require at least 3 witnesses")
        return self

def run():
    print("======================================")
    