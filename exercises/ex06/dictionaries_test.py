"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "123456789"


def test_invert_empty_dictionary() -> None:
    """This tests if the function returns an empty dictionary when original dictionary is empty."""
    original_dictionary: dict[str, str]
    original_dictionary = dict()
    assert invert(original_dictionary) == {}


def test_invert_single_key_value_pair() -> None:
    """This tests if the function returns correct dictionary with one key-value pair."""
    original_dictionary: dict[str, str]
    original_dictionary = dict()
    original_dictionary["Kaviya"] = "David"
    assert invert(original_dictionary) == {'David': 'Kaviya'}


def test_invert_multiple_pairs() -> None:
    """This tests if the function returns correct dictionary with multiple key-value pairs."""
    original_dictionary: dict[str, str]
    original_dictionary = dict()
    original_dictionary["Kaviya"] = "David"
    original_dictionary["Rose"] = "Conklin"
    original_dictionary["Jade"] = "Hughes"
    original_dictionary["Sanji"] = "Sai"
    assert invert(original_dictionary) == {'David': 'Kaviya', 'Conklin': 'Rose', 'Hughes': 'Jade', 'Sai': 'Sanji'}


def test_favorite_color_tie() -> None:
    """This tests if the function returns the most popular color that appeared first if there is a tie."""
    original_dictionary: dict[str, str]
    original_dictionary = dict()
    original_dictionary["Kaviya"] = "blue"
    original_dictionary["Rose"] = "green"
    original_dictionary["Jade"] = "green"
    original_dictionary["Sanji"] = "blue"
    assert favorite_color(original_dictionary) == "blue"


def test_favorite_color_unanimous() -> None:
    """This tests if the function returns the most popular color when everyone has the same favorite color."""
    original_dictionary: dict[str, str]
    original_dictionary = dict()
    original_dictionary["Kaviya"] = "blue"
    original_dictionary["Rose"] = "blue"
    original_dictionary["Jade"] = "blue"
    original_dictionary["Sanji"] = "blue"
    assert favorite_color(original_dictionary) == "blue"


def test_favorite_color_random() -> None:
    """This tests if the function correctly returns the most popular color when there are a variety of colors."""
    original_dictionary: dict[str, str]
    original_dictionary = dict()
    original_dictionary["Kaviya"] = "blue"
    original_dictionary["Rose"] = "yellow"
    original_dictionary["Jade"] = "green"
    original_dictionary["Sanji"] = "blue"
    original_dictionary["Oviya"] = "blue"
    original_dictionary["Charlie"] = "yellow"
    original_dictionary["Meher"] = "pink"
    assert favorite_color(original_dictionary) == "blue"


def test_count_empty_list() -> None:
    """This tests if the function returns an empty dictionary when there is an empty list."""
    a_list: list[str] = []
    assert count(a_list) == {}


def test_count_one_value() -> None:
    """This tests if the function returns correct dictionary when there are multiple duplicates of the same value."""
    a_list: list[str] = ['apple', 'apple', 'apple']
    assert count(a_list) == {'apple': 3}


def test_count_multiple_values() -> None:
    """This tests if the function returns correct dictionary when there are multiple duplicates of different values."""
    a_list: list[str] = ['apple', 'apple', 'apple', 'pear', 'orange', 'pear', 'orange', 'orange']
    assert count(a_list) == {'apple': 3, 'pear': 2, 'orange': 3}