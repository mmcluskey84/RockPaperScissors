import random


comp_wins = 0
player_wins = 0

def choose_option():
    player_choice = input("Choose one of the following options: Rock, Paper or Scissors: ")
    if player_choice in ["Rock", "rock", "R", "r"]:
        player_choice = "r"
    elif player_choice in ["Paper", "paper", "p", "P"]:
        player_choice = "p"
    elif player_choice in ["Scissors", "scissors", "S", "s"]:
        player_choice = "s"
    else:
        print("Sorry, I do not understand, please try again")
        choose_option()
    return player_choice

def computer_choice():
    comp_choice = random.randint(1,3)
    if comp_choice == 1:
        comp_choice = "r"
    elif comp_choice == 2:
        comp_choice = "p"
    elif comp_choice == 3:
        comp_choice = "s"
    return comp_choice

def score(comp_wins, player_wins):
        if player_wins > comp_wins:
            print("You are winning, it is " + str(player_wins) + " to " + str(comp_wins))
        elif player_wins < comp_wins:
            print("The computer is winning.  It is " + str(comp_wins) + " to " + str(player_wins))
        else:
            print("It is a tie! " + str(player_wins) + " all.")




while True:
    print(" ")
    user_choice = choose_option()
    AI__choice = computer_choice()
    print(" ")

    if user_choice == "r":
        if AI__choice == "r":
            print("You choose Rock.  The computer choose Rock.  It is a Tie!")
        elif AI__choice == "p":
            print("You choose Rock.  The computer choose Paper.  Paper covers Rock.  Computer wins!")
            comp_wins += 1
        elif AI__choice  == "s":
            print("You choose Rock.  The computer choose Scissors.  Rock breaks the Scissors.  You win!")
            player_wins += 1
    elif user_choice == "p":
        if AI__choice == "r":
            print("You choose Paper.  The computer Choose Rock. Paper covers Rock. You win!")
            player_wins += 1
        elif AI__choice == "p":
            print("You choose Paper.  The computer choose Paper. Its a tie!")
        elif AI__choice == "s":
            print("You choose Paper.  The computer choose Scissors.  Scissors cut Paper.  Computer wins!")
            comp_wins += 1
    else:
        if AI__choice == "r":
            print(" You choose scissors.  The computer choose Rock.  The Rock breaks Scissors.  Computer wins!")
            comp_wins += 1
        elif AI__choice == "p":
            print("You choose Scissors.  The computer choose Paper.  Scissors cut Paper.  You win!")
            player_wins += 1
        elif AI__choice == "s":
            print("You choose Scissors.  The computer choose Scissors.  Its a tie!")

    score(comp_wins, player_wins)

    another_game = input("\n\nWould you like to play again?: Yes or No ")
    if another_game in ["yes", "Yes", "y", "Y"]:
        print("\n\nOk, lets play again!")
        pass
    elif another_game in ["No", "no", "N", "n"]:
        print("Okay, thanks for player. Come back soon!")
        break
    else:
        break
    



    