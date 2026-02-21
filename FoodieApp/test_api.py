import pytest
import requests

BASE_URL = "http://localhost:5000/api/v1"

@pytest.fixture(scope="module")
def created_restaurant():
    """Fixture to ensure a restaurant exists for dish and order tests."""
    payload = {
        "name": "Test Kitchen",
        "category": "Italian",
        "location": "Downtown",
        "images": ["img1.jpg"],
        "contact": "1234567890"
    }
    response = requests.post(f"{BASE_URL}/restaurants", json=payload)
    return response.json()

# Parameterized test for multiple restaurant registrations
@pytest.mark.parametrize("name, category", [
    ("Burger King", "Fast Food"),
    ("Sushi Zen", "Japanese"),
])
def test_register_restaurant(name, category):
    payload = {
        "name": name,
        "category": category,
        "location": "Global",
        "images": ["link.jpg"],
        "contact": "000-000"
    }
    response = requests.post(f"{BASE_URL}/restaurants", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == name
    assert "id" in data  # Schema validation

def test_get_restaurant_not_found():
    response = requests.get(f"{BASE_URL}/restaurants/9999")
    assert response.status_code == 404
    assert response.json()["error"] == "Restaurant not found"

def test_add_dish(created_restaurant):
    res_id = created_restaurant["id"]
    payload = {
        "name": "Pasta Carbonara",
        "type": "Main",
        "price": 15.50,
        "available_time": "10am-10pm",
        "image": "pasta.jpg"
    }
    response = requests.post(f"{BASE_URL}/restaurants/{res_id}/dishes", json=payload)
    assert response.status_code == 201
    assert response.json()["price"] == 15.50