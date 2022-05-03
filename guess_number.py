import random

difficulty = 10 * int(input("Pick a difficulty level (1,2,3) to start the game: ")) 

def main():
    randomNumber = random.randint(1, difficulty)
    print(randomNumber)
    guess = ""
    while guess != randomNumber:
        guess = int(input(f"Guess the number! 1 to {difficulty}? "))
        if guess > randomNumber:
            print("Go more Lower!")
        elif guess < randomNumber:
            print("Go more Higher!")
        else:
            print(f"Congrats the number was {randomNumber}. You beat the game!")

main()