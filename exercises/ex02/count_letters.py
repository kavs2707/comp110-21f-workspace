"""Counting letters in a string."""

__author__ = "730316359"



what_letter: str = input("What letter do you want to search for?: ")
word: str = input("Enter a word: ")
count: str = ""
i: int = 0

if what_letter != word[i]:
    print("0")

while i < len(word): 
    if what_letter == word[i]:
        i = i + 1
        count = i

