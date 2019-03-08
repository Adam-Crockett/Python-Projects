from functools import lru_cache  # Used to cache values

# fibonacci_cache = {}
# Used for explicit use of Memoization
# You create a set and hold values at the given n location
# Reference those terms and use them instead of recalculating the result


@lru_cache(maxsize=1500)  # Used over a function to tell what returns are cached
def fibonacci(n):
    """Return the nth Fibonacci number"""

    if type(n) != int:
        raise TypeError("n must be a positive int")
    if n < 1:
        raise ValueError("n must be a positive int")

    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n - 1) + fibonacci(n - 2)


count = int(input("How many Fibonacci numbers would you like to generate? "))
for x in range(1, count + 1):
    print(fibonacci(x))
