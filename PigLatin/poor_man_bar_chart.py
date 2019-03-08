import pprint
from collections import defaultdict


def statement_request():
    entry = input("Enter a phrase for us to deconstruct:\n").lower()
    return entry


def deconstruct(entry):
    """
    Function to create a deconstructed list of the statement letters
    :param entry: The string input from user
    :return: sorted list of letters used in statement
    """
    chart = defaultdict(list)
    for letter in entry:
        if letter.isalpha():
            chart[letter].append(letter)
    return sorted(chart.items())


if __name__ == '__main__':
    print("Hello, welcome to our statement analyzer. Input a statement and we will break it down into how many letters"
          "it has.")
    print("Enter 'stop' to quit.")

    # Loop to keep asking for more statements
    while True:
        statement = statement_request()
        if statement == "stop":
            print("Thank you for using our services. Have a nice day.")
            break
        else:
            pp = pprint.PrettyPrinter(width=110)
            pp.pprint(deconstruct(statement))


