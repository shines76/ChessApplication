"""This module contains the Game class."""
import chess
from player import Human, Computer

__path__ = "C:\\Users\\ttred\\Documents\\Programming\\stockfish-windows-x86-64\\stockfish\\stockfish-windows-x86-64"


class Game:
    """Class to play chess game."""

    def __init__(self, player_team: str):
        """Initializes the game."""
        self.board = chess.Board()
        self.board.turn = chess.WHITE
        self.human = Human(player_team)

        if player_team == "white":
            computer_team = "black"
        else:
            computer_team = "white"

        self.computer = Computer(computer_team, __path__)

    def __start__(self):
        """Starts the game."""

        print("Welcome to Chess!")

        self.__play()

    def __play(self):
        """Plays the game."""

        while not self.board.is_game_over():

            self.__print_board()

            self.__play_move()

            self.computer.play(self.board)

        self.__print_board()

    def __print_board(self):
        """Prints the board."""

        print(self.board)

    def __play_move(self):
        """Plays a move."""

        move = input("What move do you want to play? ")

        self.human.play(move, self.board)

    def get_serializable(self):
        """Gets the session."""

        session_dict = dict(self.__dict__)

        session_dict["board"] = str(session_dict["board"])

        return session_dict
