"""Drawing forests in a loop."""

__author__ = "730316359"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

number: str = input("Depth: ")
depth: int = int(number)
trees = ""

i: int = 1
while i <= depth: 
    trees = TREE * i
    print(trees)
    i += 1