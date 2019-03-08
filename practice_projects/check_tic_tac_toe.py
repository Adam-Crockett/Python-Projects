
class TicTacToe:
    """Class that creates a num x num board list, default size is 3x3"""
    def __init__(self, size=3):
        self.turn_count = 0
        self.blank = " "
        self.player_x = "x"
        self.player_o = "o"
        self.board = [[self.blank for _ in range(size)] for _ in range(size)]

    def check_win(self, player):

        # Row check of board using sets
        for x in range(0, 3):
            row_check = {self.board[x][0], self.board[x][1], self.board[x][2]}
            if len(row_check) == 1 and self.board[x][0] is player:
                return True

        # Column check using sets
        for x in range(0, 3):
            col_check = {self.board[0][x], self.board[1][x], self.board[2][x]}
            if len(col_check) == 1 and self.board[0][x] is player:
                return True

        # Check each diagonal, with grid this small for loop is excessive
        diag1_check = {self.board[0][0], self.board[1][1], self.board[2][2]}
        diag2_check = {self.board[0][2], self.board[1][1], self.board[2][0]}
        if (len(diag1_check) == 1 or len(diag2_check) == 1) and self.board[1][1] is player:
            return True

        return False

    def show_board(self):
        for row in self.board:
            print("-------------")
            print("|", row[0], "|", row[1], "|", row[2], "|")

        print("-------------")


class Score:
    def __init__(self):
        self.games = 0
        self.ties = 0
        self.player_x = 0
        self.player_o = 0

    def tie_game(self):
        self.ties += 1

    def x_win(self):
        self.player_x += 1

    def o_win(self):
        self.player_o += 1

    def game_played(self):
        self.games += 1

    def show_score(self):
        print("_____Current Score of Games_____")
        print("Games Played: %s" % self.games)
        print("Player x has won: %i games." % self.player_x)
        print("Player o has won: %i games." % self.player_o)
        print("There have been %i tie games." % self.ties)
        print("_________________________________")


if __name__ == '__main__':

    scores = Score()

    while True:

        my_game = TicTacToe()
        print("Hello, welcome to the Tic Tac Toe Game! For each player enter 2 digits, row then column(ex: 1,1)")
        current_player = my_game.player_x

        while my_game.turn_count < 9:
            my_game.show_board()  # Show the board
            move = input("Player %s what is your move?\n" % current_player).split(",")  # Get player input
            try:
                # Make sure the entry lower bound is valid
                if int(move[0]) <= 0 or int(move[1]) <= 0:
                    raise IndexError
                # Find the spot on board
                spot_check = my_game.board[int(move[0]) - 1][int(move[1]) - 1]
                # Check that the spot is not taken
                if spot_check == " ":
                    # Set the spot for player
                    my_game.board[int(move[0]) - 1][int(move[1]) - 1] = current_player  # Set the marker for player

                    # See if the current player won
                    if my_game.check_win(current_player):
                        print("You won player %s!!!" % current_player)
                        if current_player == "x":
                            scores.x_win()
                        else:
                            scores.o_win()
                        my_game.show_board()  # Show the board
                        break

                    my_game.turn_count += 1  # Track for a tie

                    # Change the turn to next player
                    if current_player == "x":
                        current_player = my_game.player_o
                    else:
                        current_player = my_game.player_x
                else:
                    print("That position is already taken!")
            except ValueError:
                print("You didn't enter a valid location!")
            except IndexError:
                print("You didn't enter a valid location!")

        if my_game.turn_count >= 9:
            print("The game was a tie!")
            scores.tie_game()
            my_game.show_board()  # Show the board

        scores.game_played()
        scores.show_score()
        again = input("Play again? y or n: ").lower()
        if again == "y" or again == "yes":
            pass
        elif again == "n" or again == "no":
            print("Thanks for playing!")
            break
        else:
            print("You didn't say if you wanted to play again, bye!")

