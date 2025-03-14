# app.py
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Offerte di lavoro mockate con coordinate
job_offers = [
    {
        "id": 1,
        "title": "Sviluppatore Frontend",
        "description": "Lavoro freelance su progetti web.",
        "lat": 51.505,
        "lng": -0.09
    },
    {
        "id": 2,
        "title": "Designer UI/UX",
        "description": "Collaborazione per design di app.",
        "lat": 51.51,
        "lng": -0.1
    },
    {
        "id": 3,
        "title": "Sviluppatore Backend",
        "description": "Progetti Python e Flask.",
        "lat": 51.5074,
        "lng": -0.08
    }
]


coworking_spaces = [
    {
        "id": 1,
        "title": "Coworking1",
        "description": "Coworking1.",
        "lat": 58.505,
        "lng": -0.09
    },
    {
        "id": 2,
        "title": "Coworking2",
        "description": "Coworking2",
        "lat": 60.51,
        "lng": -0.1
    },
    {
        "id": 3,
        "title": "Coworking3",
        "description": "Coworking3",
        "lat": 51.5074,
        "lng": -1.08
    }
]

@app.route('/api/coworking_spaces', methods=['GET'])
def get_coworking_spaces():
    return jsonify(coworking_spaces)

@app.route('/api/job_offers', methods=['GET'])
def get_job_offers():
    return jsonify(job_offers)

@app.route('/api/job_offers', methods=['POST'])
def crea_offerta():
    nuova_offerta = request.get_json()
    nuova_offerta["id"] = len(job_offers) + 1
    job_offers.append(nuova_offerta)
    return jsonify(nuova_offerta), 201

if __name__ == '__main__':
    app.run(debug=True)

