import random
# Use of the sowpods, a commonly used word reference file, is for the use of academic purposes only.


if __name__ == '__main__':

        try:
            with open("sowpods", "r") as file:
                lines = file.readlines()
        except FileNotFoundError:
            print("Could not read file")
        else:
            rand_index = random.randint(0, len(lines))
            print(lines[rand_index])




