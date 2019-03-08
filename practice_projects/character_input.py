from datetime import date

# Get user input and current year
name = input("What is your name?\n")
age = int(input("What is your age?\n"))
current_year = date.today().year

# Calculate the year they turn 100
hundred_year = (100 - age) + current_year

# Message of the year they turn 100
b_day_msg = name + " your 100th birthday will be in the year " + str(hundred_year) + "!"
print(b_day_msg)

# Reprint message request
reprint = int(input("How many more times would you like to see your birthday year?\n"))

# Reprinting the message
for x in range(reprint):
    print(b_day_msg)

