"""File to define Fish class."""

__author__: str = "730483620"


class Fish:
    """Class set up for Fish!"""

    age: int

    def __init__(self):
        """Inttializing Fish!"""
        self.age = 0

    def one_day(self):
        """Increasing the age of Fish!"""
        self.age += 1
