
b_day_dictionary = {"nicola tesla": "07/10/1856", "stephen hawking": "01/08/1942", "benjamin franklin": "01/17/1706",
                    "isaac newton": "01/04/1643", "albert einstein": "03/14/1879"}


def get_value(key):
    return b_day_dictionary[key]


if __name__ == '__main__':
    entry = ""
    print("Hello, welcome to the famous scientist birthday database.\n"
          "We have the birthdays of:")
    for key in b_day_dictionary:
        print(key.title())
    print("--------------------------")
    while entry != "quit":
        try:
            entry = input("Who's birthday would you like to know?(type 'quit' to stop your search): ").lower()
        except TypeError:
            print("You did not use a valid entry.")
        else:
            if entry in b_day_dictionary:
                print("{} had their birthday on {}".format(entry.title(), b_day_dictionary[entry]))
    print("Thank you for using our birthday database!")




