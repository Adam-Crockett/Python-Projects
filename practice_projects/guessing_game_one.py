import random


counter = 0
number = random.randint(1, 9)
guess = ""

while str(guess) != "exit":

    guess = input("Guess a number between 1 and 9(enter exit to stop playing): ")

    if str(guess).lower() == "exit":
        break
    elif int(guess) > number:
        print("You guessed too high.")
        counter += 1
    elif int(guess) < number:
        print("You guessed too low.")
        counter += 1
    else:
        counter += 1
        print("You guessed correctly! It took you", counter, "tries.")
        print("...\nPicking a new number.\n...")
        number = random.randint(1, 9)
        counter = 0

print("Game Over! You guessed", counter,  "times.")
