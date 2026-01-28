from flask import Flask, jsonify, request, abort

app = Flask(__name__)

users = [
    {"id": 1, "name": "Gaurav", "role": "Admin"},
    {"id": 2, "name": "Sumit", "role": "User"}
]

def get_next_id():
    return max(user["id"] for user in users) + 1 if users else 1


@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user is None:
        abort(404, description="User not found")
    return jsonify(user), 200


@app.route('/users', methods=['POST'])
def create_user():
    if not request.json or 'name' not in request.json:
        abort(400, description="Missing 'name' in request body")

    new_user = {
        "id": get_next_id(),
        "name": request.json['name'],
        "role": request.json.get('role', 'User')
    }

    users.append(new_user)
    return jsonify(new_user), 201


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user is None:
        abort(404, description="User not found")

    if not request.json:
        abort(400, description="Request body must be JSON")

    user["name"] = request.json.get("name", user["name"])
    user["role"] = request.json.get("role", user["role"])

    return jsonify(user), 200


@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": error.description}), 404


@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": error.description}), 400


if __name__ == '__main__':
    app.run(debug=True)
