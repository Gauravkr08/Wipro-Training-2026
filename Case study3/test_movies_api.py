import requests

BASE_URL = "http://127.0.0.1:5000/api"

def test_get_all_movies():
    response = requests.get(f"{BASE_URL}/movies")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_add_movie():
    payload = {
        "id": 102,
        "movie_name": "Inception",
        "language": "English",
        "duration": "2h 28m",
        "price": 300
    }
    response = requests.post(f"{BASE_URL}/movies", json=payload)
    assert response.status_code == 201
    assert response.json()["movie_name"] == "Inception"

def test_get_movie_by_id():
    response = requests.get(f"{BASE_URL}/movies/101")
    assert response.status_code == 200
    assert response.json()["movie_name"] == "Interstellar"

def test_book_ticket():
    payload = {
        "movie_id": 101,
        "tickets": 2
    }
    response = requests.post(f"{BASE_URL}/bookings", json=payload)
    assert response.status_code == 201
    assert response.json()["status"] == "CONFIRMED"
