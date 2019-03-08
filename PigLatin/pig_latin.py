"""A Simple Pig Latin Translator"""


def ask_for_phrase():
    phrase = input("Please enter a phrase to translate in to pig latin:\n").lower()
    return phrase


def check_phrase(phrase):
    word_list = phrase.rsplit(" ")
    for word in word_list:
        if not word.isalpha():
            return False
    else:
        return True


def pig_latin(phrase):
    """
    Function to translate into pig latin
    :param phrase: The user input
    :return: Print the pig latin translation
    """
    vowel = ("a", "e", "i", "o", "u")
    pig_list = []
    word_list = phrase.rsplit(" ")

    for word in word_list:
        # Check if the word starts with a vowel
        if word.startswith(vowel):
            pig_list.append(word + "way")
        # Check if the first two letters are consonants
        elif not word.startswith(vowel) and not word.startswith(vowel, 1):
            start = word[0:2]
            pig_list.append(word[2:] + start + "ay")
        # If only the first letter is a consonant
        else:
            start = word[0]
            pig_list.append(word[1:] + start + "ay")

    return print(" ".join(pig_list))


if __name__ == '__main__':
    print("Hello, welcome to the Pig Latin Translator\n")
    print("Enter 'done' to exit.")

    # Loop to continue until the user enters "done"
    while True:
        entry = ask_for_phrase()

        if not check_phrase(entry):
            print("You did not enter a valid input, please use letters only.")
        elif entry == "done":
            print("Thank you for using our translator.")
            break
        else:
            pig_latin(entry)
