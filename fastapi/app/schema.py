import uuid
from typing import Optional
from pydantic import BaseModel, Field


class Farmer(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)
    contact: str = Field(...)
    location: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "name": "John Smith",
                "contact": "XXX-YYY-ZZZZ",
                "location": "..."
            }
        }


class FarmerUpdate(BaseModel):
    name: Optional[str]
    contact: Optional[str]
    location: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "name": "John Smith",
                "contact": "XXX-YYY-ZZZZ",
                "location": "XXX Adams Blvd., Los Angeles, CA 90007"
            }
        }
