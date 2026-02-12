from flask import Flask, request, jsonify

app = Flask(__name__)

patients = []

@app.route("/api/patients", methods=["GET"])
def get_patients():
    return jsonify(patients), 200

@app.route("/api/patients", methods=["POST"])
def add_patient():
    data = request.json
    if not data or "name" not in data:
        return jsonify({"error": "Patient name is required"}), 400
    patients.append(data)
    return jsonify({"message": "Patient registered successfully"}), 201

@app.route("/api/patients/<int:pid>", methods=["GET"])
def get_patient(pid):
    return jsonify(patients[pid]), 200

@app.route("/api/patients/<int:pid>", methods=["PUT"])
def update_patient(pid):
    patients[pid].update(request.json)
    return jsonify({"message": "Patient updated successfully"}), 200

if __name__ == "__main__":
    app.run(debug=True)
