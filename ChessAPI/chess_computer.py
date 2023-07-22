"""Module to play chess against a computer."""
import chess
import chess.engine

__path__ = "C:\\Users\\ttred\\Documents\\Programming\\stockfish-windows-x86-64\\stockfish\\stockfish-windows-x86-64"


def init_engine():
    """Initializes the chess engine."""
    engine = chess.engine.SimpleEngine.popen_uci(__path__)
    engine.configure({"Skill Level": 1})
    return engine


def start(team: str):
    """Starts the chess game."""
    engine = init_engine()
    board = chess.Board()

    if team == "white":
        player_team = chess.WHITE
    else:
        player_team = chess.BLACK
    board.turn = player_team
    board.push_san("e4")

    result = engine.play(board=board,
                         limit=chess.engine.Limit(time=0.1))
    board.push(result.move)

    print(board)


def play(move: str):
    """Plays a move."""
    pass


print("Welcome to Chess!")
start(input("What team do you want to be? (white/black) "))
