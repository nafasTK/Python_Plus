#rock - paper - scissors
b = True

name1 = input("please enter your name : ")
name2 = "computer"

a = int(input("how many rounds do you want to play : "))

player1_score = 0
player2_score = 0

print("rock")
print("paper")
print("scissors")


while b == True :

    import random
   
    randomNumber = random.randint(0,2)
    computerMove = "rock"

    if randomNumber == 0:
        computerMove = "rock"
    elif randomNumber == 1:
        computerMove = "paper"
    elif randomNumber == 2:
        computerMove = "scissors"

    player1 = input(f"{name1} please make your move : ")
    print(f"{name2} please make your move : {computerMove}")
    player2 = computerMove

    if player1 == "rock" and player2 == "scissors":
        print (f"{name1} wins !")
        print(" ")
        player1_score = player1_score + 1

    elif player1 == "rock" and player2 == "paper":
        print(f"{name2} wins !")
        print(" ")
        player2_score = player2_score + 1

    elif player1 == "paper" and player2 == "rock":
        print(f"{name1} wins !")
        print(" ")
        player1_score = player1_score + 1

    elif player1 == "paper" and player2 == "scissors":
        print(f"{name2} wins !")
        print(" ")
        player2_score = player2_score + 1

    elif player1 == "scissors" and player2 == "paper":
        print(f"{name1} wins !")
        print(" ")
        player1_score = player1_score + 1

    elif player1 == "scissors" and player2 == "rock":
        print(f"{name2} wins !")
        print(" ")
        player2_score = player2_score + 1

    elif player1 == player2:
        print ("thats a tie !")
        print(" ")

    else:
        print(" ")
        print("something went wrong !")
        print(" ")

    if player1_score == a or player2_score == a :
        b = False
        if player1_score == a :
            print(" ")
            print(f"{name1} win the game !")
        elif player2_score == a :
            print(" ")
            print(f"{name2} win the game !")
        break

input ()
