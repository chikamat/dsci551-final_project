from fastapi.encoders import jsonable_encoder
from typing import List
from schema import Farmer, FarmerUpdate


def create_farmer_db(database, farmer: Farmer):
    farmer = jsonable_encoder(farmer)
    new_farmer = database["farmers"].insert_one(farmer)
    return database["farmers"].find_one({"_id": new_farmer.inserted_id})


def list_farmers_db(database) -> List[Farmer]:
    return list(database["farmers"].find(limit=100))


def find_farmer_db(database, id: str) -> Farmer:
    return database["farmers"].find_one({"_id": id})


def update_farmer_db(database, id: str, farmer: FarmerUpdate):
    farmer = {k: v for k, v in farmer.dict().items() if v is not None}
    database["farmers"].update_one({"_id": id}, {"$set": farmer})
    return database["farmers"].find_one({"_id": id})


def delete_farmer_db(database, id: str):
    return database["farmers"].delete_one({"_id": id}).deleted_count
