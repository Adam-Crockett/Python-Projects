import random
# Use of the sowpods, a commonly used word reference file, is for the use of academic purposes only.


class Hangman:

    def __init__(self):
        self.guess_list = set()
        self.word = []
        self.progress_word = []
        self.guess_count = 6

    def man_print(self):
        """Print the hangman's current state, max 6 guesses."""
        if self.guess_count == 6:
            print("______")
            print("|    |")
            print("|")
            print("|")
            print("|")
            print("|")
            print("-------------")
        elif self.guess_count == 5:
            print("______")
            print("|    |")
            print("|    O")
            print("|")
            print("|")
            print("|")
            print("-------------")
        elif self.guess_count == 4:
            print("______")
            print("|    |")
            print("|    O")
            print("|    |")
            print("|")
            print("|")
            print("-------------")
        elif self.guess_count == 3:
            print("______")
            print("|    |")
            print("|    O")
            print("|   /|")
            print("|")
            print("|")
            print("-------------")
        elif self.guess_count == 2:
            print("______")
            print("|    |")
            print("|    O")
            print("|   /|\\")
            print("|")
            print("|")
            print("-------------")
        elif self.guess_count == 1:
            print("______")
            print("|    |")
            print("|    O")
            print("|   /|\\")
            print("|   /")
            print("|")
            print("-------------")
        elif self.guess_count == 0:
            print("______")
            print("|    |")
            print("|    O")
            print("|   /|\\")
            print("|   / \\")
            print("|")
            print("-------------")

    def get_file(self, path):
        """Open file and create a list of the lines."""
        try:
            with open(path, "r") as file:
                lines = file.readlines()
        except FileNotFoundError:
            print("Could not find your file.")
        else:
            return lines

    def rand_index_word(self, lines):
        """Select a random line in the file, set it as the word."""
        rand_index = random.randint(0, len(lines))
        self.word = [letter for letter in lines[rand_index].strip().lower()]

    def show_word_chart(self):
        """Display the current known parts of the word."""
        display = []
        for x in self.word:
            if x in self.guess_list:
                display.append(x)
            else:
                display.append("_")
        self.progress_word = display

        print(" ".join(display))
        print("***********************************")

    def guess_check(self, guess):
        """Checks if the guest letter is in the word."""
        if guess in self.guess_list:
            return print("You already guessed that letter.")
        elif guess in self.word:
            self.guess_list.add(guess)
            return print("%s is in the word." % guess)
        else:
            self.guess_list.add(guess)
            self.guess_count -= 1
            return print("Your %s guess is not in the word." % guess)

    def win_check(self):
        """See if the user has completely guessed the word"""
        if self.progress_word == self.word:
            return True
        else:
            return False


if __name__ == '__main__':
    again = True
    while again:
        print("Welcome to the Hangman guessing game!")
        hang = Hangman()
        hang.rand_index_word(hang.get_file("sowpods"))
        while hang.guess_count != 0 and not hang.win_check():
            try:
                attempt = str(input("Guess a letter in the word: ")).lower()
                if len(attempt) != 1:
                    raise TypeError
            except TypeError:
                print("You didn't enter a single letter.")
            else:
                hang.guess_check(attempt)
                if hang.win_check():
                    print("Yeah! You got the word! Good Job!")

            finally:
                hang.man_print()
                hang.show_word_chart()

        # Verify if the player wants to play again.
        entry = "  "
        while len(entry) != 1:
            try:
                entry = str(input("Would you like to play again? (y or n): ")).lower()
            except ValueError:
                print("You did not enter a valid input.")
            else:
                if entry == "n":
                    print("Thanks for playing! Good Bye!")
                    again = False
                elif entry == "y":
                    print("Ok, lets go again!")
                else:
                    print("Not a valid input.")
