import random

difficulty = int(input("Pick a difficulty level (1,2,3) to start the game"))
guess = int(input(f"What is your guess 1 to {difficulty * 10}? "))

def randomizer():
    hardness = difficulty * 10
    number = random.randint(1, hardness)
    return number

answer = randomizer()

if guess == answer:
    print(f"You win! {answer} is the true answer.")
else:
    print(f"You lose! {answer} was the true answer.")