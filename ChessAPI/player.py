"""Chess library"""
import chess
import chess.engine


class Player:
    """Player of chess game."""

    def __init__(self, team: str):
        """Initializes the player."""
        self.team = team


class Human(Player):
    """Human player for chess game."""

    def play(self, move: str, board: chess.Board):
        """Plays a move."""
        # Set the team to the player's team
        board.turn = self.team

        if move in board.legal_moves:
            board.push_san(move)
        else:
            raise ValueError("Move is not legal.")

        return board


class Computer(Player):
    """Computer player for chess game."""

    def __init__(self, team: str, path: str):
        """Initializes the computer player."""
        super().__init__(team)
        self.__engine = self.__init_engine(path)

    def __init_engine(self, path: str):
        """Initializes the chess engine."""

        engine = chess.engine.SimpleEngine.popen_uci(path)
        engine.configure({"Skill Level": 1})
        return engine

    def get_serializable(self):
        """Gets the session."""
        session_dict = {}
        session_dict["team"] = self.team
        return session_dict

    def play(self, board: chess.Board):
        """Plays a move."""
        # Set the team to the computer's team
        board.turn = self.team

        move = self.__engine.play(board=board,
                                  limit=chess.engine.Limit(time=0.1))

        if move in board.legal_moves:
            board.push_san(move)
        else:
            raise ValueError("Move is not legal.")

        return board
