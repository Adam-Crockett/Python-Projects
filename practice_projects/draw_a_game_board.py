

class Board:
    """The class that defines a board"""

    def __init__(self, input_size=1):
        self.size = input_size
        self.create_board_list()

    def create_board_list(self):
        """Create a board 2d list"""
        verticals = " ---"
        middle = " "
        horizontals = "| " + middle + " "

        for index in range(self.size):
            print(verticals * self.size)
            print(horizontals * self.size + "|")
        print(verticals * self.size)


if __name__ == '__main__':
    try:
        entry = int(input("Enter a board size: "))
        if entry <= 0:
            raise ValueError
        else:
            new_board = Board(entry)
    except ValueError:
        print("You did not enter a valid size.")


