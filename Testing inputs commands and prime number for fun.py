
player1 = input ("Please state your name player 1: ")
while True:
    if any (char.isdigit() for char in player1):
        print ("Please do not include digits in your name.")
        player1 = input ("Please state your name player 1: ")
    else:
        break

player2 = input ("Player 2, please state your name: ")

while True:
    if any (char.isdigit() for char in player2):
        print ("Please do not include digits in your name.")
        player2 = input("Player 2, please state your name: ")
    elif player2 == player1:
        print("Choose different names.")
        player2 = input("Player 2, please state your name: ")
    else:
        break

#allowedinputs = "rock", "Rock", "scissors", "Scissors", "paper", "Paper"

print ("Welcome ", player1, " and ", player2, " let's begin the game!")

# player1InputAttempt = 1
# while True:
#     player1Input = input (player1 + " please choose one of the 3 listed options: rock, paper or scissors: ")
#     if player1Input.lower == "rock" or "scissors" or "paper":
#         break
#     else:
#         print ("Please type in the options with a lower or upper case. ")
#         print ("You're currently at attempt: ", player1InputAttempt)
#         player1InputAttempt = player1InputAttempt + 1
#
# player2InputAttempt = 1
# while True:
#     player2Input = input(player2 + " please choose one of the 3 listed options: rock, paper or scissors: ")
#     if player2Input.lower == "rock" or "scissors" or "paper":
#         break
#     else:
#         print("Please type in the options with a lower or upper case. ")
#         print ("You're currently at attempt: ", player2InputAttempt)
#         player1InputAttempt = player2InputAttempt + 1

player1InputAttempt = 1
player2InputAttempt = 1
score1 = 0
score2 = 0
#needs help
while score1 or score2 != 3:
    while True:
        player1Input = input(player1 + " please choose one of the 3 listed options: rock, paper or scissors: ")
        if player1Input == "rock" or "scissors" or "paper":
            break
        else:
            print("Please type in the options with a lower or upper case. ")
            print("You're currently at attempt: ", player1InputAttempt)
            player1InputAttempt = player1InputAttempt + 1

    while True:
        player2Input = input(player2 + " please choose one of the 3 listed options: rock, paper or scissors: ")
        if player2Input == "rock" or "scissors" or "paper":
            break
        else:
            print("Please type in the options with a lower or upper case. ")
            print("You're currently at attempt: ", player2InputAttempt)
            player1InputAttempt = player2InputAttempt + 1

    player1Input = player1Input.lower()
    player2Input = player2Input.lower()


    print("test1")
    if score1 == 3:
            print("Good job ", player1, ", you won!")
            break

    elif score2 == 3:
            print("Good job ", player2, ", you won!")
            break

    elif player1Input.lower == player2Input.lower:
            print("Good job you drew, go again.")

    elif player1Input == "rock" or player2Input == "scissors":
            score1 = score1 + 1
            print(score1, " : ", score2)

    elif player1Input == "paper" and player2Input == "rock":
            score1 = score1 + 1
            print(score1, " : ", score2)

    elif player1Input == "scissors" and player2Input == "paper":
            score1 = score1 + 1
            print(score1, " : ", score2)

    elif player2Input == "rock" and player1Input == "scissors":
            score2 = score2 + 1
            print(score1, " : ", score2)

    elif player2Input == "paper" and player1Input == "rock":
            score2 = score2 + 1
            print(score1, " : ", score2)

    elif player2Input == "scissors" and player1Input == "paper":
            score2 = score2 + 1
            print(score1, " : ", score2)


    #else:
        #print ("Good job!")
        #break

    else:
        play_again = input("Would you like to go again? (y/n): ")
        if play_again != "y":
            break
        else:
            score1 = 0
            score2 = 0

print ("Thank you for playing.")



