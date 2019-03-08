import random
import string


def pwd_gen(size=8, chars=string.ascii_letters + string.digits + string.punctuation):
    return "".join(random.choice(chars) for _ in range(size))


print(pwd_gen(int(input("How long would you like your password?: "))))
