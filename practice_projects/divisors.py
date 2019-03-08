num = int(input("Pick a number:"))

print([x for x in range(1, num + 1) if num % x == 0])

