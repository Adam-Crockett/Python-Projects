entry = input("Enter 3 values, separate with a space: ").split(" ")

if len(entry) == 3:
    try:
        largest = int(entry[0])
        for x in entry:
            if int(x) > largest:
                largest = int(x)
        print(largest)
    except ValueError:
        print("Need integers only please!")
else:
    print("Your list of values is the wrong size!")
