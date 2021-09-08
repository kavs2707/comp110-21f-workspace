"""Repeat a beat!"""

__author__ = "730316359"


beat: str = input("What beat do you want to repeat? ")
number: str = input("How many times do you want to repeat it? ")
x: int = int(number)
repeated_word: str = ""


if x <= 0:
    print("No beat...")
else:
    i: int = 0
    while i < x - 1: 
        repeated_word = repeated_word + beat + " " 
        i = i + 1

    repeated_word = repeated_word + beat
    print(repeated_word)
