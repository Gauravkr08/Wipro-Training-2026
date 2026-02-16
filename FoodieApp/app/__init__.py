from flask import Flask
from app.routes.restaurant_routes import restaurant_bp
from app.routes.dish_routes import dish_bp
from app.routes.admin_routes import admin_bp
from app.routes.user_routes import user_bp
from app.routes.order_routes import order_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(restaurant_bp, url_prefix="/api/v1/restaurants")
    app.register_blueprint(dish_bp, url_prefix="/api/v1/dishes")
    app.register_blueprint(admin_bp, url_prefix="/api/v1/admin")
    app.register_blueprint(user_bp, url_prefix="/api/v1/users")
    app.register_blueprint(order_bp, url_prefix="/api/v1/orders")
    return app