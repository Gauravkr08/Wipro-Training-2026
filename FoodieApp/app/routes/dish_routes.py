from flask import Blueprint, request, jsonify
from app.services.dish_service import DishService

dish_bp = Blueprint("dish", __name__)
service = DishService()

@dish_bp.post("/")
def add_dish():
    return jsonify(service.add_dish(request.json)), 201

@dish_bp.put("/<int:dish_id>")
def update_dish(dish_id):
    r = service.update_dish(dish_id, request.json)
    if r: return jsonify(r), 200
    return jsonify({"error":"Dish not found"}), 404

@dish_bp.put("/<int:dish_id>/status")
def toggle_dish(dish_id):
    r = service.toggle_dish(dish_id)
    if r: return jsonify(r), 200
    return jsonify({"error":"Dish not found"}), 404

@dish_bp.delete("/<int:dish_id>")
def delete_dish(dish_id):
    r = service.delete_dish(dish_id)
    if r: return jsonify({"message":"Dish deleted"}), 200
    return jsonify({"error":"Dish not found"}), 404