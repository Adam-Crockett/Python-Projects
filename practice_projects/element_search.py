

def binary_search(arr, x, start=0, end=None):
    """Binary list search if value exists in set"""
    if end is None:
        end = len(arr) - 1
    if start > end:
        return False

    mid = (start + end) // 2

    if x == arr[mid]:
        return True
    elif x < arr[mid]:
        return binary_search(arr, x, start, mid - 1)
    else:
        return binary_search(arr, x, mid + 1, end)


if __name__ == '__main__':

    entry = ""
    entry_list = []

    while entry != "stop":
        entry = input("Enter a value to add to your list. (Enter 'stop' to end entry): ")
        if entry != "stop":
            try:
                entry = int(entry)
            except ValueError:
                print("You didn't enter a number")
            else:
                entry_list.append(entry)

    entry = ""
    entry_list.sort()
    print(entry_list)

    while entry != "stop":
        entry = input("What number to you want to see is in the list?('stop' to exit): ")
        if entry != "stop":
            try:
                entry = int(entry)
            except ValueError:
                print("You didn't enter a number")
            else:
                if binary_search(entry_list, entry):
                    print("Your number is in the list.")
                else:
                    print("Your number is not in the list.")

