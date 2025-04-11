"""File to define Bear class."""

__author__: str = "730483620"


class Bear:
    """Setting up Bear Class!"""

    age: int
    hunger_score: int

    def __init__(self):
        """Initializing Bear!"""
        self.age = 0
        self.hunger_score = 0

    def one_day(self):
        """Increasing age and hunger of Bear!"""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int):
        """Bear Eats Fish!"""
        self.hunger_score += num_fish
