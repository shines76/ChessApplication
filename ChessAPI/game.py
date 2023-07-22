import chess
from player import Player


class Game:
    """Class to play chess game."""

    def __init__(self, player_team: str):
        """Initializes the game."""
        self.board = chess.Board()
        self.board.turn = chess.WHITE
        self.player1 = Player(player_team, "human")

        if player_team == "white":
            computer_team = "black"
        else:
            computer_team = "white"
        self.player2 = Player(computer_team, "computer")
