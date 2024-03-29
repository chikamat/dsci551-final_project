import uuid
from typing import Optional, Dict
from pydantic import BaseModel, Field


class Product(BaseModel):
    inventory: Optional[int]
    price: Optional[float]
    rating: Optional[float]
    review_count: int = 0

    class Config:
        extra = "forbid"


class Farmer(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)
    contact: str = Field(...)
    location: str = Field(...)
    product_list: Optional[Dict[str, Product]]

    class Config:
        extra = "forbid"
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "name": "John Smith",
                "contact": "XXX-YYY-ZZZZ",
                "location": "...",
                "product_list": {
                    "tomato": {"inventory": 10, "price": 5, "rating": 4.3},
                    "potato": {"inventory": 35, "price": 2, "rating": 3.2}
                }
            }
        }


class FarmerUpdate(BaseModel):
    contact: Optional[str]
    location: Optional[str]
    product_list: Optional[Dict[str, Product]]

    class Config:
        extra = "forbid"
        schema_extra = {
            "example": {
                "contact": "XXX-YYY-ZZZZ",
                "location": "XXX Adams Blvd., Los Angeles, CA 90007",
                "product_list": {
                    "tomato": {"inventory": 12, "price": 5.5, "rating": 4.5}
                }
            }
        }


class Purchase(BaseModel):
    quantity: int = Field(...)

    class Config:
        extra = "forbid"
        schema_extra = {
            "example": {
                "quantity": 2,
            }
        }


class Review(BaseModel):
    rating: float = Field(...)

    class Config:
        extra = "forbid"
        schema_extra = {
            "example": {
                "rating": 3.5,
            }
        }
