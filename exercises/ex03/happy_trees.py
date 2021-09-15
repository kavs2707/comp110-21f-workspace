"""Drawing forests in a loop."""

__author__ = "730316359"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

number: str = input("Depth: ")
depth: int = int(number)
trees = TREE


if depth <= 0:
    print("")
else:
    i: int = 0
    while i < depth: 
        trees = TREE * depth
        print(trees)
        j: int = 0
        while j < depth:
            trees = trees + TREE * depth
            print(trees)
            j += 1
    i += 1 
