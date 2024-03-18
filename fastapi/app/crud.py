from fastapi.encoders import jsonable_encoder
from typing import List
from app.schema import Farmer, FarmerUpdate


def hash_name(name):
    return sum(map(ord, name)) % 2


def find_database_with_farmer(database_list, id: str):
    for db in database_list:
        if db["farmers"].find_one({"_id": id}):
            return db
    return None


def create_farmer_db(database_list, farmer: Farmer):
    database = database_list[hash_name(farmer.dict().get('name'))]
    farmer = jsonable_encoder(farmer)
    new_farmer = database["farmers"].insert_one(farmer)
    return database["farmers"].find_one({"_id": new_farmer.inserted_id})


def list_farmers_db(database_list) -> List[Farmer]:
    return list(database_list[0]["farmers"].find()) + list(database_list[1]["farmers"].find())


def find_farmer_db(database_list, id: str) -> Farmer:
    for db in database_list:
        farmer = db["farmers"].find_one({"_id": id})
        if farmer:
            return farmer
    return None


def update_farmer_db(database_list, id: str, farmer: FarmerUpdate):
    db = find_database_with_farmer(database_list, id)
    if db is None:
        return None
    update_data = {k: v for k, v in farmer.dict().items() if v is not None}
    db["farmers"].update_one({"_id": id}, {"$set": update_data})
    return db["farmers"].find_one({"_id": id})


def delete_farmer_db(database_list, id: str):
    db = find_database_with_farmer(database_list, id)
    if db is None:
        return 0
    return db["farmers"].delete_one({"_id": id}).deleted_count
