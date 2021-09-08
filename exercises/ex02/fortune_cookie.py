"""Fortune Cookie Machine!"""

__author__ = "730316359"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


print("Your fortune cookie says...")
random_number: int = randint(1, 4)

if random_number <= 2: 
    if random_number == 1:
        print("Your day is going to be amazing!")
    else: 
        print("You are going to meet a very important person today!")
else:
    if random_number == 3:
        print("You are going to learn an important lesson.")
    else:
        print("Your day might not start off great, but keep your head up!")
    
print("Now, go seize the day!")