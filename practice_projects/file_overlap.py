

def compare_lists(l_one, l_two):
    """Create new list based on values that are in both input lists."""
    return [num for num in l_one if num in l_two]


if __name__ == '__main__':

    file_one = input("Enter file name of FIRST number list(must be single int per line): ")
    file_two = input("Enter file name of SECOND number list(must be single int per line): ")

    with open(file_one, "r") as open_file:
        list_one = [int(x) for x in open_file]

    with open(file_two, "r") as open_file:
        list_two = [int(x) for x in open_file]

    print(compare_lists(list_one, list_two))
    # print(overlap_list)  # Could just print here, we dont need to create a file

   # with open("overlap_numbers", "w") as open_file:  # Create a file to output results for practice
    #    for x in overlap_list:
     #       open_file.write(str(x) + "\n")
      #      print(x)


