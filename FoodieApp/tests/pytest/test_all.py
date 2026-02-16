import requests

BASE_REST = "http://localhost:5000/api/v1/restaurants"
BASE_DISH = "http://localhost:5000/api/v1/dishes"
BASE_USER = "http://localhost:5000/api/v1/users"
BASE_ORDER = "http://localhost:5000/api/v1/orders"
BASE_ADMIN = "http://localhost:5000/api/v1/admin"

# Restaurant
def test_add_restaurant():
    resp = requests.post(BASE_REST+"/", json={"name":"Food Hub","category":"Fast"})
    assert resp.status_code == 201

def test_update_restaurant():
    resp = requests.put(BASE_REST+"/1", json={"name":"Updated"})
    assert resp.status_code in [200,404]

def test_disable_restaurant():
    resp = requests.put(BASE_REST+"/1/dis")
    assert resp.status_code in [200,404]

def test_get_restaurant():
    resp = requests.get(BASE_REST+"/1")
    assert resp.status_code in [200,404]

# Dish
def test_add_dish():
    resp = requests.post(BASE_DISH+"/", json={"name":"Pizza","type":"Main","price":100})
    assert resp.status_code == 201

def test_update_dish():
    resp = requests.put(BASE_DISH+"/1", json={"price":120})
    assert resp.status_code in [200,404]

def test_toggle_dish():
    resp = requests.put(BASE_DISH+"/1/status")
    assert resp.status_code in [200,404]

def test_delete_dish():
    resp = requests.delete(BASE_DISH+"/1")
    assert resp.status_code in [200,404]

# User
def test_register_user():
    resp = requests.post(BASE_USER+"/register", json={"name":"Alice","email":"a@b.com","password":"123"})
    assert resp.status_code in [201,409]

def test_search_restaurant():
    resp = requests.get(BASE_USER+"/search?name=&location=&dish=&rating=")
    assert resp.status_code == 200

# Order
def test_place_order():
    resp = requests.post(BASE_ORDER+"/", json={"user_id":1,"restaurant_id":1,"dishes":[1]})
    assert resp.status_code == 201

def test_give_rating():
    resp = requests.post(BASE_ORDER+"/ratings", json={"order_id":1,"rating":5,"comment":"Great"})
    assert resp.status_code == 201

def test_view_orders_user():
    resp = requests.get(BASE_ORDER+"/1")
    assert resp.status_code == 200

def test_view_orders_restaurant():
    resp = requests.get(BASE_ORDER+"/restaurant/1")
    assert resp.status_code == 200

# Admin
def test_approve_restaurant():
    resp = requests.put(BASE_ADMIN+"/restaurants/1/approve")
    assert resp.status_code == 200

def test_disable_restaurant_admin():
    resp = requests.put(BASE_ADMIN+"/restaurants/1/disable")
    assert resp.status_code == 200

def test_view_feedback():
    resp = requests.get(BASE_ADMIN+"/feedback")
    assert resp.status_code == 200

def test_view_orders_admin():
    resp = requests.get(BASE_ADMIN+"/orders")
    assert resp.status_code == 200