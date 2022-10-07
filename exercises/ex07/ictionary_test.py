"""EX07 - Unit tests for  Dictionary Functions."""
__author__ = "730578788"

from dictionary import invert, favorite_color, count
import pytest


with pytest.raises(KeyError):
    my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
    invert(my_dictionary)


def test_invert_empty() -> None:
    """Tests edge case for empty dictionary."""
    dictionary: dict[str, str] = {}
    assert invert(dictionary) == {}


def test_invert_single_letters() -> None:
    """Tests used case for dictionary of single letter keys and values."""
    dictionary: dict[str, str] = {'a': 'z', 'b' : 'y', 'c': 'x'}
    assert invert(dictionary) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_strings() -> None:
    """Tests used case for dictionary of word string keys and values"""
    dictionary: dict[str, str] = {"apple" : "cinnamon", "strawberry": "banana"}
    assert invert(dictionary) == {"cinnamon" : "apple", "banana" : "strawberry"}


def test_favorite_color_multiple() -> None:
    """Tests edge case when there's a tie for the most popular color."""
    name_and_colors: dict[str, str] = {"Max": "green", "Bob": "blue", "Jack": "blue", "James": "green"}
    assert favorite_color(name_and_colors) == "green"


def test_favorite_color_pink() -> None:
    """Tests used case when pink is the single most popular color."""
    name_and_colors: dict[str, str] = {"Max": "green", "Bob": "pink", "Jack": "pink", "James": "black"}
    assert favorite_color(name_and_colors) == "pink"


def test_favorite_color_green() -> None:
    """Tests used case when red is the single most popular color."""
    name_and_colors: dict[str, str] = {"Max": "red", "Bob": "red", "Jack": "red", "James": "black"}
    assert favorite_color(name_and_colors) == "red"


def test_count_empty() -> None:
    """Tests edge case when the input list is empty."""
    word_list: list[str] = []
    assert count(word_list) == {}


def test_count_frequent_strings() -> None:
    """Tests used case where the input list contains values that appear more than once."""
    word_list: list[str] = ["apple", "goat", "corn", "corn", "apple", "apple"]
    assert count(word_list) == {'apple' : 3, 'goat' : 1, 'corn' : 2}


def test_count_same_number() -> None:
    """Tests used case where the input list contains values that each appear the same number of times."""
    word_list: list[str] = ["dog", "cow", "pig", "dog", "cow", "pig"]
    assert count(word_list) == {'dog' : 2, 'cow' : 2, 'pig' : 2}