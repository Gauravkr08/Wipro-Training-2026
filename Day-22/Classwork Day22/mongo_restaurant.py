from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["restaurant_db"]

collection = db["restaurants"]

new_restaurant = {
    "name": "Spice Villa",
    "location": "Bhubaneswar",
    "category": "Indian",
    "rating": 4.5
}

insert_result = collection.insert_one(new_restaurant)

print("Inserted Restaurant ID:", insert_result.inserted_id)

print("Inserted Document:")
print(collection.find_one({"_id": insert_result.inserted_id}))

