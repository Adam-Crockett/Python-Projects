
def list_duplicate_remover(a_list):
    """Parse through a list and remove duplicates returning the new list"""

    new_list = []
    for x in a_list:
        if x not in new_list:
            new_list.append(x)
    return new_list


def list_set_convert(a_list):
    """Convert from list to set, in order to remove duplicates, then back to list for return"""

    return list(set(a_list))


the_list = [1, 2, 3, 4, 5, 5, 1, 7, 18]
print(list_set_convert(the_list))
print(list_duplicate_remover(the_list))
