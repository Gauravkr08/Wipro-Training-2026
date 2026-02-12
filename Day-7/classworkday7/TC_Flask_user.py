from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data
users = [
    {"id": 1, "name": "Raja"},
    {"id": 2, "name": "Rama"}
]

# Home route
@app.route("/", methods=["GET"])
def home():
    return "Welcome to User API"


# Get all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200


# Get single user
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify(user), 200
    return jsonify({"message": "User not found"}), 404


# Add new user
@app.route("/users", methods=["POST"])
def add_user():
    data = request.json

    if not data or "name" not in data:
        return jsonify({"error": "Name is required"}), 400

    new_id = max(user["id"] for user in users) + 1 if users else 1

    new_user = {
        "id": new_id,
        "name": data["name"]
    }

    users.append(new_user)
    return jsonify(new_user), 201


# Update entire user (PUT)
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.json

    if not data or "name" not in data:
        return jsonify({"error": "Name is required"}), 400

    for user in users:
        if user["id"] == user_id:
            user["name"] = data["name"]
            return jsonify(user), 200

    return jsonify({"message": "User not found"}), 404


# Update partial user (PATCH)
@app.route("/users/<int:user_id>", methods=["PATCH"])
def patch_user(user_id):
    data = request.json

    if not data:
        return jsonify({"error": "Request body required"}), 400

    for user in users:
        if user["id"] == user_id:
            if "name" in data:
                user["name"] = data["name"]
            return jsonify(user), 200

    return jsonify({"message": "User not found"}), 404


# Delete user
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return jsonify({"message": "User deleted successfully"}), 200

    return jsonify({"message": "User not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
