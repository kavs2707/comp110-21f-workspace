"""Practice with dictionaries."""

__author__ = "730316359"

# Define your functions below


def main() -> None: 
    """Entrypoint of program."""


def invert(original_dictionary: dict[str, str]) -> dict[str, str]:
    """This function inverts the keys and values of a given dictionary."""
    inverted_dictionary = dict()
    for key in original_dictionary:
        if original_dictionary[key] in inverted_dictionary:
            raise KeyError("KeyError")
        inverted_dictionary[original_dictionary[key]] = key
    return inverted_dictionary


def favorite_color(original_dictionary: dict[str, str]) -> str:
    """This function determines the favorite color among a dictionary of names and colors."""
    frequency: dict[str, int] = dict()
    color: str = ""
    number: int = 0
    for key in original_dictionary: 
        if original_dictionary[key] in frequency:
            frequency[original_dictionary[key]] += 1
        else:
            frequency[original_dictionary[key]] = 1
    for key in frequency: 
        if number < frequency[key]:
            number = frequency[key]
            color = key
    return color

       
def count(a_list: list[str]) -> dict[str, int]:
    """This function counts the number of times a value appears in a list and generates a dictionary."""
    frequency = dict[str, int]
    frequency = dict()
    for item in a_list:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency


if __name__ == "__main__":
    main()