

def check_prime(num):
    """Checks if a number is prime"""
    divisors = [x for x in range(2, num) if num % x == 0]
    if num > 1:
        if len(divisors) == 0:
            print("The number is prime!")
        else:
            print("The number is not prime.")
    else:
        print("The number is not prime.")


number = int(input("Enter a number to check for primality: "))
check_prime(number)
