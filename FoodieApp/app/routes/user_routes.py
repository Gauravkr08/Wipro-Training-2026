from flask import Blueprint, request, jsonify
from app.services.user_service import UserService

user_bp = Blueprint("user", __name__)
service = UserService()

@user_bp.post("/register")
def register_user():
    r = service.register_user(request.json)
    if r: return jsonify(r), 201
    return jsonify({"error":"Conflict"}), 409

@user_bp.get("/search")
def search_restaurant():
    return jsonify(service.search_restaurant()), 200