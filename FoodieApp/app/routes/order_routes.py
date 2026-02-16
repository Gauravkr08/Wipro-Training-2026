from flask import Blueprint, request, jsonify
from app.services.order_service import OrderService

order_bp = Blueprint("order", __name__)
service = OrderService()

@order_bp.post("/")
def place_order():
    return jsonify(service.place_order(request.json)), 201

@order_bp.post("/ratings")
def give_rating():
    return jsonify({"message":"Rating added","data":request.json}), 201

@order_bp.get("/<int:user_id>")
def view_orders_by_user(user_id):
    return jsonify(service.view_orders_by_user(user_id)), 200

@order_bp.get("/restaurant/<int:restaurant_id>")
def view_orders_by_restaurant(restaurant_id):
    return jsonify(service.view_orders_by_restaurant(restaurant_id)), 200