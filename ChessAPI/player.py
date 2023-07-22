"""Player class for chess game"""


class Player:
    """Player of chess game."""

    def __init__(self, team: str, typeof: str):
        """Initializes the player."""
        self.team = team
        self.typeof = typeof
