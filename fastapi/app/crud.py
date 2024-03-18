from fastapi.encoders import jsonable_encoder
from typing import List
from app.schema import Farmer, FarmerUpdate


def hash_name(name):
    return sum(map(ord, name)) % 2


def create_farmer_db(database_list, farmer: Farmer):
    database = database_list[hash_name(farmer.dict().get('name'))]
    farmer = jsonable_encoder(farmer)
    new_farmer = database["farmers"].insert_one(farmer)
    return database["farmers"].find_one({"_id": new_farmer.inserted_id})


def list_farmers_db(database_list) -> List[Farmer]:
    return list(database_list[0]["farmers"].find()) + list(database_list[1]["farmers"].find())


def find_farmer_db(database_list, id: str) -> Farmer:
    if database_list[0]["farmers"].find_one({"_id": id}) is None:
        return database_list[1]["farmers"].find_one({"_id": id})
    else:
        return database_list[0]["farmers"].find_one({"_id": id})


def update_farmer_db(database_list, id: str, farmer: FarmerUpdate):
    farmer = {k: v for k, v in farmer.dict().items() if v is not None}
    if database_list[0]["farmers"].find_one({"_id": id}) is not None:
        database_list[0]["farmers"].update_one({"_id": id}, {"$set": farmer})
        return database_list[0]["farmers"].find_one({"_id": id})
    elif database_list[1]["farmers"].find_one({"_id": id}) is not None:
        database_list[1]["farmers"].update_one({"_id": id}, {"$set": farmer})
        return database_list[1]["farmers"].find_one({"_id": id})
    else:
        return None


def delete_farmer_db(database_list, id: str):
    if database_list[0]["farmers"].find_one({"_id": id}) is not None:
        return database_list[0]["farmers"].delete_one({"_id": id}).deleted_count
    elif database_list[1]["farmers"].find_one({"_id": id}) is not None:
        return database_list[1]["farmers"].delete_one({"_id": id}).deleted_count
    else:
        return 0
