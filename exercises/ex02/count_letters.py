"""Counting letters in a string."""

__author__ = "730316359"



letter: str = input("What letter do you want to search for?: ")
word: str = input("Enter a word: ")

counter: int = 0
while counter < len(word): 
    if letter == word[counter]:
        count = len(word[counter])
        counter = counter + 1
        count = len(word[counter]) + 1
        print(count)