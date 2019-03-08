keep_playing = True


while keep_playing:
    player_one = input("Player one: Enter rock, paper, or scissors: ").lower()
    player_two = input("Player two: Enter rock, paper, or scissors: ").lower()

    if player_one == player_two:
        print("Game is a tie.")
    elif player_one == "rock" and player_two != "paper":
        print("Player one wins!")
    elif player_one == "paper" and player_two != "scissor":
        print("Player one wins!")
    elif player_one == "scissors" and player_two != "rock":
        print("Player one wins!")
    else:
        print("Player two wins!")

    again = input("Would you like to play again? y or n: ").lower()
    if again == "n":
        keep_playing = False


