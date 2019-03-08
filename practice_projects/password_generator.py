import random
import string


def upper_letter_gen():
    """Pick upper case letters to add to password"""
    return random.choice(string.ascii_uppercase)
    # return string.ascii_uppercase[random.randrange(0, len(string.ascii_uppercase))]


def lower_letter_gen():
    """Pick lower case letters to add to password"""
    return random.choice(string.ascii_lowercase)


def number_gen():
    """Pick numbers to add to password"""
    return random.choice(string.digits)


def symbol_gen():
    """Pick symbols to add to password"""
    return random.choice(string.punctuation)


def pick_length(choice):
    """Return what the length of the password should be"""
    if choice == "weak":
        return random.randint(7, 9)
    else:
        return random.randint(10, 15)


if __name__ == '__main__':
    """Main to run the password generator"""
    size = 0
    while size == 0:
        pick = str(input("Would you like a (weak or strong) password?")).lower()
        if pick.lower() == "weak":
            size = pick_length("weak")
        elif pick.lower() == "strong":
            size = pick_length("strong")
        else:
            print("You did not choose a valid entry.")

    pwd_builder = []

    while size != 0:
        picker = random.randint(1, 4)

        if picker == 1:
            pwd_builder.append(upper_letter_gen())
        elif picker == 2:
            pwd_builder.append(lower_letter_gen())
        elif picker == 3:
            pwd_builder.append(number_gen())
        elif picker == 4:
            pwd_builder.append(symbol_gen())

        size -= 1

    random.shuffle(pwd_builder)
    pwd_builder = "".join(pwd_builder)
    print("Your created password is:", pwd_builder)

