

"""Ask the user for a number"""
number = int(input("What number would you like us to check?\n"))
if number % 2 == 0:
    print(number,  "is even.")
    if number % 4 == 0:
        print(number, "is also a multiple of 4.")
else:
    print(number, "is odd.")


"""Ask the user what divisor they want us to try"""
divisor = int(input("What number would you like us to see divides into " + str(number) + "?\n"))

if number % divisor == 0:
    print(divisor, "divides into", number)
else:
    print(divisor, "does not divide into", number)

