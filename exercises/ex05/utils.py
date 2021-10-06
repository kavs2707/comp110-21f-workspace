"""List utility functions part 2."""

__author__ = "730316359"

# Define your functions below


def only_evens(x: list[int]) -> list[int]:
    """This function returns a list containing only the even elements of the input list."""
    y: list[int] = []
    i = 0 
    while i < len(x):
        if x[i] % 2 == 0: 
            y.append(x[i])
        i += 1
    return y


def sub(a_list: list[int], start: int, end: int) -> list[int]: 
    """This function generates the values between the start index and end index of a list."""
    y: list[int] = []
    if len(a_list) == 0 or start >= len(a_list) or end <= 0: 
        return y
    end = end - 1
    while start <= end:
        if end >= len(a_list): 
            end = len(a_list) - 1
            y.append(a_list[start])
        else: 
            if start > 0: 
                y.append(a_list[start])
            else: 
                start = 0
                y.append(a_list[start])
        start += 1
    return y


def concat(one: list[int], two: list[int]) -> list[int]:
    """This list generates a new list that contains all of the elements of the first list followed by all of the elements of the second list."""
    new_list: list[int] = []
    i = 0
    while i < len(one):
        new_list.append(one[i])
        i += 1
    i = 0
    while i < len(two):
        new_list.append(two[i])
        i += 1
    return new_list
