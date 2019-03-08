a = [5, 10, 15, 20, 25]
b = [2, 3, 4]


def cut_list(a_list):
    """Cuts a list into the first and last element."""
    if len(a_list) == 0:
        return "Empty list"
    return [a_list[0], a_list[-1]] if len(a_list) > 1 else a_list[0]


print(cut_list(b))
