"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730316359"


def test_only_evens_empty() -> None:
    """This tests if the function returns empty list when there are no even numbers."""
    x: list[int] = [1, 3, 5, 7, 9]
    assert only_evens(x) == []


def test_only_evens_single_item() -> None:
    """This tests if the function returns the only even number in the list."""
    x: list[int] = [1, 3, 4, 5, 7]
    assert only_evens(x) == [4]


def test_only_evens_multiple_items() -> None:
    """This tests if the function returns all even numbers in the list."""
    x: list[int] = [2, 4, 6, 8, 9]
    assert only_evens(x) == [2, 4, 6, 8]


def test_sub_start_index_greater_than_or_equal_to_length_of_list() -> None:
    """This tests if the function returns an empty list if the start index is greater than or equal to the length of the list."""
    a_list: list[int] = [1, 2, 3, 4, 5]
    start: int = 7
    end: int = 9
    assert sub(a_list, start, end) == []


def test_sub_part_of_the_list() -> None:
    """This tests if the function returns values in between the index values."""
    a_list: list[int] = [1, 2, 3, 4, 5]
    start: int = 1
    end: int = 4
    assert sub(a_list, start, end) == [2, 3, 4]


def test_sub_whole_list() -> None:
    """This tests if the function returns the whole list with the appropriate index values."""
    a_list: list[int] = [1, 2, 3, 4, 5]
    start: int = 0
    end: int = 5
    assert sub(a_list, start, end) == [1, 2, 3, 4, 5]


def test_concat_two_empty_lists() -> None:
    """This tests if the function returns an empty list when both lists are empty."""
    one: list[int] = []
    two: list[int] = []
    assert concat(one, two) == []


def test_concat_two_lists_of_same_length() -> None:
    """This tests if the function generates both lists together when they are of equal length."""
    one: list[int] = [1, 2, 3]
    two: list[int] = [9, 8, 7]
    assert concat(one, two) == [1, 2, 3, 9, 8, 7]


def test_concat_two_lists_of_different_lengths() -> None:
    """This tests if the function generates both lists together when they are of different lengths."""
    one: list[int] = [1, 2, 3]
    two: list[int] = [9]
    assert concat(one, two) == [1, 2, 3, 9]