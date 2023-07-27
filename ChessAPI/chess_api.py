"""Application to play chess game"""

import json
from flask_cors import CORS
from flask import Flask, request, jsonify
from game import Game


class GameEncoder(json.JSONEncoder):
    """JSON encoder for Game object"""

    def default(self, obj):
        if isinstance(obj, Game):
            # Convert the Game object to a dictionary representation
            return obj.get_serializable()
        return json.JSONEncoder.default(self, obj)


app = Flask(__name__)
app.secret_key = "your_secret_key"
CORS(app)
app.json_encoder = GameEncoder


@app.route("/start", methods=["POST"])
def start_game():
    """Starts the game."""

    # Get the team from the request
    team = request.json["team"]

    # Start the game

    game = Game(team)

    if game.board.turn:
        turn = "white"
    else:
        turn = "black"

    data = {
        "message": "Hello from Chess API!",
        "human-team": game.human.team,
        "computer-team": game.computer.team,
        "board": str(game.board),
        "turn": turn,
        "game-over": game.board.is_game_over(),
        "result": game.board.result(),
        "legal-moves": str(game.board.legal_moves),
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
