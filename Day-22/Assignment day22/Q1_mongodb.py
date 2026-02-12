from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["company_db"]
collection = db["employees"]

new_employee = {
    "name": "Harsh",
    "department": "CSE",
    "salary": 60000
}

collection.insert_one(new_employee)
print("\nNew employee inserted in MongoDB!")

print("\nEmployees in CSE department:")
for emp in collection.find({"department": "CSE"}):
    print(emp)

collection.update_one(
    {"name": "Harsh"},
    {"$set": {"salary": 70000}}
)

print("\nSalary updated successfully!")
