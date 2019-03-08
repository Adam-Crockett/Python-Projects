a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

ask = int(input("Pick a number:\n"))

print([x for x in a if x < ask])
