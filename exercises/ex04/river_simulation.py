"""Simulation driver for the River ecosystem."""

__author__: str = "730483620"

from exercises.EX04.river import River


# A River object with 10 Fish and 2 Bears
my_river = River(num_fish=10, num_bears=2)


# Intial State
my_river.view_river()

# Simulation after one week
my_river.one_river_week()
