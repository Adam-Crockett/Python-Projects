def ask_for_string():
    """Ask the user for a series of words"""
    return input("Please enter a bunch of words: ")


def string_reverser(a_string):
    """Return reversed word order of string"""
    a_list = a_string.split()
    a_list.reverse()
    return " ".join(a_list)


entry = ask_for_string()
print(string_reverser(entry))
