
from flask import Blueprint, jsonify

admin_bp = Blueprint("admin", __name__)
admin_restaurants = {}

@admin_bp.put("/restaurants/<int:restaurant_id>/approve")
def approve_restaurant(restaurant_id):
    admin_restaurants[restaurant_id] = "approved"
    return jsonify({"message":"Restaurant approved"}), 200

@admin_bp.put("/restaurants/<int:restaurant_id>/disable")
def disable_restaurant(restaurant_id):
    admin_restaurants[restaurant_id] = "disabled"
    return jsonify({"message":"Restaurant disabled"}), 200

@admin_bp.get("/feedback")
def view_feedback():
    return jsonify([{"user":"John","comment":"Great!"}]), 200

@admin_bp.get("/orders")
def view_orders():
    return jsonify([{"order_id":1,"status":"delivered"}]), 200