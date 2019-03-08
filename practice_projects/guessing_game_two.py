import time

print("Let me guess your number. Pick a value between 0 and 100. Get Ready!")
count = 1
time.sleep(2)
table = [x for x in range(101)]
guess = table[50]

while True:

    if len(table) == 1:
        print("Your number must be", table[0])
        print("I got the answer in", count)
        break

    ask = input("Is your number " + str(guess) + "? Enter yes, high, or low: ").lower()
    print(ask)

    if ask == "yes":
        print("Woot! I got the answer! Thanks for playing with me.")
        print("I got the answer in", count, "tries.")
        break
    elif ask == "high":
        table = [x for x in range(min(table), guess)]

        guess = table[len(table) // 2]
        count += 1
    elif ask == "low":
        table = [x for x in range(guess + 1, max(table) + 1)]

        guess = table[len(table) // 2]
        count += 1
    else:
        print("I dont understand.")
