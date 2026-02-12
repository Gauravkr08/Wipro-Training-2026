from flask import Flask, jsonify, request

app = Flask(__name__)

movies = [
    {
        "id": 101,
        "movie_name": "Interstellar",
        "language": "English",
        "duration": "2h 49m",
        "price": 250
    }
]

bookings = []

# GET all movies
@app.route("/api/movies", methods=["GET"])
def get_movies():
    return jsonify(movies), 200

# GET movie by ID
@app.route("/api/movies/<int:movie_id>", methods=["GET"])
def get_movie(movie_id):
    movie = next((m for m in movies if m["id"] == movie_id), None)
    if movie:
        return jsonify(movie), 200
    return jsonify({"error": "Movie not found"}), 404

# POST add movie
@app.route("/api/movies", methods=["POST"])
def add_movie():
    data = request.get_json()
    if not data or "id" not in data:
        return jsonify({"error": "Invalid data"}), 400
    movies.append(data)
    return jsonify(data), 201

# PUT update movie
@app.route("/api/movies/<int:movie_id>", methods=["PUT"])
def update_movie(movie_id):
    data = request.get_json()
    movie = next((m for m in movies if m["id"] == movie_id), None)
    if not movie:
        return jsonify({"error": "Movie not found"}), 404
    movie.update(data)
    return jsonify(movie), 200

# DELETE movie
@app.route("/api/movies/<int:movie_id>", methods=["DELETE"])
def delete_movie(movie_id):
    global movies
    movie = next((m for m in movies if m["id"] == movie_id), None)
    if not movie:
        return jsonify({"error": "Movie not found"}), 404
    movies = [m for m in movies if m["id"] != movie_id]
    return jsonify(movie), 200

# POST booking
@app.route("/api/bookings", methods=["POST"])
def book_ticket():
    data = request.get_json()
    if "movie_id" not in data or "tickets" not in data:
        return jsonify({"error": "Invalid booking data"}), 400
    booking = {
        "booking_id": len(bookings) + 1,
        "movie_id": data["movie_id"],
        "tickets": data["tickets"],
        "status": "CONFIRMED"
    }
    bookings.append(booking)
    return jsonify(booking), 201

if __name__ == "__main__":
    app.run(debug=True)
