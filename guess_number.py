import random

difficulty = int(input("Pick a difficulty level (1,2,3) to start the game"))

if difficulty == 1:
    hardness = 10
elif difficulty == 2:
    hardness = 20
else:
    hardness = 30

number = random.randint(0,hardness)
guess = int(input(f"What is your guess 1 to {hardness}? "))

if guess == number:
    print(f"You win! {number} is the true answer.")
else:
    print(f"You lose! {number} was the true answer.")