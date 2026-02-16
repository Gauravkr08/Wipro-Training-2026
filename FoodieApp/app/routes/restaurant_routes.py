from flask import Blueprint, request, jsonify
from app.services.restaurant_service import RestaurantService

restaurant_bp = Blueprint("restaurant", __name__)
service = RestaurantService()

@restaurant_bp.post("/")
def add_restaurant():
    return jsonify(service.add_restaurant(request.json)), 201

@restaurant_bp.put("/<int:restaurant_id>")
def update_restaurant(restaurant_id):
    r = service.update_restaurant(restaurant_id, request.json)
    if r: return jsonify(r), 200
    return jsonify({"error":"Restaurant not found"}), 404

@restaurant_bp.put("/<int:restaurant_id>/dis")
def disable_restaurant(restaurant_id):
    if service.disable_restaurant(restaurant_id):
        return jsonify({"message":"Restaurant disabled"}), 200
    return jsonify({"error":"Restaurant not found"}), 404

@restaurant_bp.get("/<int:restaurant_id>")
def get_restaurant(restaurant_id):
    r = service.get_restaurant(restaurant_id)
    if r: return jsonify(r), 200
    return jsonify({"error":"Restaurant not found"}), 404