

from random import randint


l = ["Rock", "Paper", "Scissors"]


computer = l[randint(0,2)]


user = False

while user == False:

    user = input("Rock, Paper, Scissors?")
    if user == computer:
        print("Tie!")
    elif user == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif user == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif user == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
   
    user = False
    computer = t[randint(0,2)]
