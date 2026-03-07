from enum import Enum
from datetime import datetime
from pydantic import BaseModel, Field, model_validator


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
            raise ValueError("High signal strength "
                             "requires a received message")
        if (self.contact_type == ContactType.telepathic and
                self.witness_count < 3):
            raise ValueError("Telepathic contacts "
                             "require at least 3 witnesses")
        return self


def run():
    print("Alien Contact Log Validation")
    print("======================================")
    print("Valid contact report:")
    alien_contact = AlienContact(
        contact_id="AC12345",
        timestamp=datetime.now(),
        location="Unknown",
        contact_type=ContactType.physical,
        signal_strength=8.0,
        duration_minutes=10,
        witness_count=5,
        message_received="Hello, Yassine!",
        is_verified=True
    )
    print(f"ID: {alien_contact.contact_id}")
    print(f"Type: {alien_contact.contact_type.value}")
    print(f"Location: {alien_contact.location}")
    print(f"Signal: {alien_contact.signal_strength}")
    print(f"Duration: {alien_contact.duration_minutes}")
    print(f"Witness: {alien_contact.witness_count}")
    print(f"Message: {alien_contact.message_received}")
    print("======================================")
    try:
        alien_contact2 = AlienContact(
            contact_id="AC12345",
            timestamp=datetime.now(),
            location="Unknown",
            contact_type=ContactType.telepathic,
            signal_strength=8.0,
            duration_minutes=10,
            witness_count=2,
            message_received="Hello, Yassine!"
        )
        print(alien_contact2)
    except Exception as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"])


run()
