"""Counting letters in a string."""

__author__ = "730316359"


what_letter: str = input("What letter do you want to search for?: ")
word: str = input("Enter a word: ")

i: int = 0

while i < len(word): 
    individual_letters: str = (word[i])
    if individual_letters == what_letter:
        print(individual_letters == what_letter)
    else: 
        print("0")
    i = i + 1