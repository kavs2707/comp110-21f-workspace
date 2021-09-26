"""Number Guessing Game!"""

__author__ = "730316359"


from random import randint


def main() -> None:
    """Entrypoint of program."""


n: int = randint(1, 10)

victory_emoji: str = '\U0001f600'

greet: str = input("Welcome to the Number Guessing Game! Guess the number from 1 - 10 in 5 tries. Are you ready to play? Enter Yes or No: ")

if greet == "Yes": 
    player: str = input("What is your name? ")
    guess: str = input(f"Okay, { player }, let's play! Guess a number between 1 - 10: ")
    first_guess: int = int(guess)
    if n == first_guess:
        print(f"You are correct! The number was { n }. Good job, { player } { victory_emoji }")
    else:
        i: int = 0
        while i < 4: 
            if first_guess != n:
                next_guess: str = input(f"Uh oh, you are wrong { player }. Try again! Enter a new guess: ")
                new_guess: int = int(next_guess)
                i += 1
            else:
                print(f"Good job, { player }. The number was { n }, you guessed correctly { victory_emoji }")
        print(f"Looks like you used all 5 tries. The number was { n }. Game over")
else: 
    print("Okay, logging out. ")
           

if __name__ == "__main__":
    main()
