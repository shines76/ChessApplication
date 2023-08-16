"""Application to play chess game"""

import json
from flask_cors import CORS
from flask import Flask, request, jsonify
from game import Game

app = Flask(__name__)
app.secret_key = "your_secret_key"
CORS(app)


@app.route("/start", methods=["POST"])
def start_game():
    """Starts the game."""

    # Get the team from the request
    team = request.json["team"]

    # Start the game

    game = Game(team)

    data = {
        "message": "Hello from Chess API!",
        "game": game.get_serializable(),
        "boardString": str(game.board)
    }

    return jsonify(data)


@app.route('/api/move', methods=['POST'])
def make_move():
    """Plays a move"""
    data = request.get_json()
    return data


@app.route('/api/board', methods=['GET'])
def get_board():
    """Gets the board"""
    data = request.get_json()
    return data


if __name__ == '__main__':
    app.run()
