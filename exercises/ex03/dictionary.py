"""Practicing Dictionary Functions in COMP 110"""

__author__ = "730483620"


def invert(input: dict[str, str]) -> dict[str, str]:
    output: dict[str, str] = {}
    for key, value in input.items():
        if value in output:
            raise KeyError("Duplicate value")
        output[value] = key

    return output


def count(elements: list[str]) -> dict[str, int]:
    outcome: dict[str, int] = {}

    for item in elements:
        if item in outcome:
            outcome[item] += 1
        else:
            outcome[item] = 1

    return outcome


def favorite_color(favs: dict[str, str]) -> str:
    """Returns the most frequently occuring favorite color"""
    colors = [color for color in favs.values()]
    count_colors = count(colors)

    max_count = 0
    most_frequent = ""

    for color in colors:
        if count_colors[color] > max_count:
            max_count = count_colors[color]
            most_frequent = color

    return most_frequent


def bin_len(terms: list[str]) -> dict[int, set[str]]:
    """Bins strings by their lengths into a dictionary with lengths as keys and sets of strings as values."""
    bins: dict[int, set[str]] = {}

    for word in terms:
        length = len(word)
        if length not in bins:
            bins[length] = set()
        bins[length].add(word)

    return bins
