import random


def check_guess(entry):
    """Checks if the user entered a 4 digit value"""
    try:
        if len(entry) == 4:
            for x in entry:
                if not isinstance(x, int):
                    return False
        else:
            print("You did not enter a 4 digit value.")
            return False
    except ValueError:
        print("You did not enter a 4 digit value.")
    else:
        return True


def cows_bulls(user_guess, r_value):
    """Return how many cow and bull values there are"""
    cows = len([x for x, y in zip(user_guess, r_value) if x == y])
    bulls = 4 - cows
    return win(cows, bulls)


def win(cows, bulls):
    if cows == 4:
        return True
    else:
        print("There are", cows, "cows and", bulls, "bulls.")
        return False


if __name__ == '__main__':
    print("Hello! Welcome to the Cows and Bulls guessing game! Guess a 4 digit number.\n\
          You get a cow if a correct digit is guessed in the correct spot.\n\
          You get a bull for a wrong entry. Happy Guessing!")

    value = [int(x) for x in str(random.randint(1000, 9999))]
    guess_count = 0

    while True:
        guess = input("Guess a 4 digit value:\n")
        try:
            guess = [int(x) for x in guess]
        except ValueError:
            print("You did not enter a 4 digit value.")
        else:
            if check_guess(guess):
                guess_count += 1
                if cows_bulls(guess, value):
                    print("You won the game in", guess_count, "tries!")
                    break



