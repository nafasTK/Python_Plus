#rock - paper - scissors
b = True

name1 = input("please enter your name : ")
name2 = "computer"

a = int(input("how many rounds do you want to play : "))

player1_score = 0
player2_score = 0

print(" ")
print("left")
print("right")
print(" ")

while b == True :

    import random
   
    randomNumber = random.randint(0,1)
    computerMove = "a"

    if randomNumber == 0:
        computerMove = "left"
    elif randomNumber == 1:
        computerMove = "right"

    player1 = input(f"{name1} please make your move : ")
    print(" ")
    print (f"{name1} : I guess {player1} is gol ")
    print(f"{name2} : {computerMove} is gol ")
    player2 = computerMove
    print(" ")
    
    if player1 == "left" and player2 == "right":
        print ("pooch !")
        print(" ")
        player2_score = player2_score + 1

    elif player1 == "right" and player2 == "left":
        print("pooch !")
        print(" ")
        player2_score = player2_score + 1

    elif player1 == player2:
        print ("gol !")
        print(" ")
        player1_score = player1_score + 1

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
