"""Counting letters in a string."""

__author__ = "730316359"


what_letter: str = input("What letter do you want to search for?: ")
word: str = input("Enter a word: ")

i: int = 0

while i < len(word): 
    letters: str = (what_letter[i])
    if word == letters:
       print(word == letters) 
    i = i + 1