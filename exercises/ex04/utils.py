"""List utility functions."""

__author__ = "730316359"


def all(x: list[int], y: int) -> bool:
    """This function indicates whether or not all the ints in the list are the same as the given int. """
    if len(x) == 0:
        return False
    i = 0
    while i < len(x):
        if x[i] != y:
            return False
        i += 1
    return True


def is_equal(x: list[int], y: list[int]) -> bool:
    """This function indicates whether or not every element at every index is equal in both lists. """
    if len(x) != len(y):
        return False
    i = 0
    while i < len(x):
        if x[i] != y[i]:
            return False
        i += 1
    return True


def max(input: list[int]) -> int:
    """This function returns the largest integer in the list. """
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    i = 0
    max = input[0]
    while i < len(input):
        if input[i] > max: 
            max = input[i]
        i += 1
    return max
