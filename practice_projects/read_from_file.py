

# Parse through each line until the _
# If that value is not in the dictionary add it and increment it by 1
# Else increase the value in the dictionary by 1
# Once at EoF print the dictionary keys and values

# Use of practicepython.org practice files are strictly for academic use.


file_types = {}

with open("training_01", "r") as open_file:
    for line in open_file:
        for x in line:
            if x == "_":
                f_type = line[0:line.index(x)]
                if f_type in file_types:
                    file_types[f_type] += 1
                else:
                    file_types[f_type] = 1

for x, y in file_types.items():
    print(x, ":",  y)


