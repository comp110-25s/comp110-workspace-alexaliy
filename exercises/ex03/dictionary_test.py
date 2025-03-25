"""Testing dicitionary functions in COMP 110"""

__author__ = "730483620"

from exercises.ex03.dictionary import invert, favorite_color, count, bin_len

import pytest


def test_invert_use_1() -> None:
    """Test use cases for invert function"""
    assert invert({"blue": "hair", "red": "purse"}) == {"hair": "blue", "purse": "red"}


def test_invert_use_2() -> None:
    """Test use cases for invert function"""
    assert invert({"tar": "heel", "sour": "patch", "green": "leaves"}) == {
        "heel": "tar",
        "patch": "sour",
        "leaves": "green",
    }


def test_invert_edge() -> None:
    """Test edge case for invert function"""
    assert invert({}) == {}


def test_invert_key_error() -> None:
    "Test for KeyError"
    with pytest.raises(KeyError):
        my_dictionary = {"blue": "hair", "red": "hair"}
        invert(my_dictionary)


def test_count_edge() -> None:
    """Test edge case for count function"""
    assert count([]) == {}


def test_count_use_1() -> None:
    """Test use cases for count function"""
    assert count(["soda"]) == {"soda": 1}


def test_count_use_2() -> None:
    """Test use cases for count function"""
    assert count(["soda", "pop", "pop", "soda"]) == {"soda": 2, "pop": 2}


def test_favorite_color_edge() -> None:
    """Test edge case for favorite_color function"""
    favs = {}
    assert favorite_color(favs) == ""


def test_favorite_color_use_1() -> None:
    """Test use cases for count function"""
    favs = {"Alexis": "blue", "Porsche": "pink", "Katy": "blue", "Sephora": "pink"}
    assert favorite_color(favs) == "blue"


def test_favorite_color_use_2() -> None:
    """Test use cases for count function"""
    assert (
        favorite_color(
            {"Alexis": "blue", "Porsche": "pink", "Tom": "blue", "Sierra": "blue"}
        )
        == "blue"
    )


def test_bin_len_edge() -> None:
    """Test edge case for bin_len function"""
    assert bin_len([]) == {}


def test_bin_len_use_1() -> None:
    """Test uses cases for bin_len function"""
    terms = ["wash", "cell", "line"]
    assert bin_len(terms) == {4: {"wash", "cell", "line"}}


def test_bin_len_use_2() -> None:
    """Test uses case for bin_len function"""
    terms = ["unc", "bye", "money", "mouse"]
    assert bin_len(terms) == {3: {"unc", "bye"}, 5: {"money", "mouse"}}
