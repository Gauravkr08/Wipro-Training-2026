from flask import Flask, request, jsonify

app = Flask(__name__)

restaurants = {}
users = {}
orders = {}
ratings = {}

restaurant_counter = 1
dish_counter = 1
user_counter = 1
order_counter = 1
rating_counter = 1

@app.route("/api/v1/restaurants", methods=["POST"])
def register_restaurant():
    global restaurant_counter
    data = request.json
    for r in restaurants.values():
        if r["name"] == data["name"]:
            return jsonify({"error": "Restaurant already exists"}), 409
    restaurant = {
        "id": restaurant_counter,
        "name": data["name"],
        "category": data["category"],
        "location": data["location"],
        "contact": data["contact"],
        "status": "pending",
        "dishes": []
    }
    restaurants[restaurant_counter] = restaurant
    restaurant_counter += 1
    return jsonify(restaurant), 201

@app.route("/api/v1/restaurants/<int:restaurant_id>", methods=["GET"])
def view_restaurant(restaurant_id):
    if restaurant_id not in restaurants:
        return jsonify({"error": "Not found"}), 404
    return jsonify(restaurants[restaurant_id]), 200

@app.route("/api/v1/restaurants/<int:restaurant_id>", methods=["PUT"])
def update_restaurant(restaurant_id):
    if restaurant_id not in restaurants:
        return jsonify({"error": "Not found"}), 404
    restaurants[restaurant_id].update(request.json)
    return jsonify(restaurants[restaurant_id]), 200

@app.route("/api/v1/restaurants/<int:restaurant_id>/disable", methods=["PUT"])
def disable_restaurant(restaurant_id):
    if restaurant_id not in restaurants:
        return jsonify({"error": "Not found"}), 404
    restaurants[restaurant_id]["status"] = "disabled"
    return jsonify({"message": "Restaurant disabled"}), 200

@app.route("/api/v1/restaurants/<int:restaurant_id>/dishes", methods=["POST"])
def add_dish(restaurant_id):
    global dish_counter
    if restaurant_id not in restaurants:
        return jsonify({"error": "Restaurant not found"}), 404
    dish = {"id": dish_counter, "restaurant_id": restaurant_id, **request.json, "enabled": True}
    restaurants[restaurant_id]["dishes"].append(dish)
    dish_counter += 1
    return jsonify(dish), 201

@app.route("/api/v1/dishes/<int:dish_id>", methods=["PUT"])
def update_dish(dish_id):
    for r in restaurants.values():
        for d in r["dishes"]:
            if d["id"] == dish_id:
                d.update(request.json)
                return jsonify(d), 200
    return jsonify({"error": "Not found"}), 404

@app.route("/api/v1/dishes/<int:dish_id>/status", methods=["PUT"])
def toggle_dish(dish_id):
    for r in restaurants.values():
        for d in r["dishes"]:
            if d["id"] == dish_id:
                d["enabled"] = request.json.get("enabled", True)
                return jsonify({"message": "Status updated"}), 200
    return jsonify({"error": "Not found"}), 404

@app.route("/api/v1/dishes/<int:dish_id>", methods=["DELETE"])
def delete_dish(dish_id):
    for r in restaurants.values():
        for d in r["dishes"]:
            if d["id"] == dish_id:
                r["dishes"].remove(d)
                return jsonify({"message": "Deleted"}), 200
    return jsonify({"error": "Not found"}), 404

@app.route("/api/v1/users/register", methods=["POST"])
def register_user():
    global user_counter
    data = request.json
    for u in users.values():
        if u["email"] == data["email"]:
            return jsonify({"error": "Exists"}), 409
    user = {"id": user_counter, **data}
    users[user_counter] = user
    user_counter += 1
    return jsonify(user), 201

@app.route("/api/v1/orders", methods=["POST"])
def place_order():
    global order_counter
    order = {"id": order_counter, **request.json, "status": "placed"}
    orders[order_counter] = order
    order_counter += 1
    return jsonify(order), 201

@app.route("/api/v1/users/<int:user_id>/orders", methods=["GET"])
def user_orders(user_id):
    return jsonify([o for o in orders.values() if o["user_id"] == user_id]), 200

@app.route("/api/v1/restaurants/<int:restaurant_id>/orders", methods=["GET"])
def res_orders(restaurant_id):
    return jsonify([o for o in orders.values() if o["restaurant_id"] == restaurant_id]), 200

@app.route("/api/v1/ratings", methods=["POST"])
def give_rating():
    global rating_counter
    if request.json["order_id"] not in orders: return jsonify({"error": "No order"}), 404
    rating = {"id": rating_counter, **request.json}
    ratings[rating_counter] = rating
    rating_counter += 1
    return jsonify(rating), 201

@app.route("/api/v1/admin/restaurants/<int:restaurant_id>/approve", methods=["PUT"])
def approve(restaurant_id):
    if restaurant_id not in restaurants: return jsonify({"error": "Not found"}), 404
    restaurants[restaurant_id]["status"] = "approved"
    return jsonify({"message": "Approved"}), 200

@app.route("/api/v1/admin/restaurants/<int:restaurant_id>/disable", methods=["PUT"])
def admin_disable(restaurant_id):
    if restaurant_id not in restaurants: return jsonify({"error": "Not found"}), 404
    restaurants[restaurant_id]["status"] = "disabled"
    return jsonify({"message": "Disabled"}), 200

@app.route("/api/v1/admin/orders", methods=["GET"])
def admin_orders():
    return jsonify(list(orders.values())), 200

if __name__ == "__main__":
    app.run(debug=True)