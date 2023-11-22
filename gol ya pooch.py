#gol ya pooch
print ("This is gol ya pooch game")
name = input("please enter your name: ")

print ("left : 1")
print ("right : 2")


import random
rand = (random.randint(1,2))

if rand == 1 :
    player = int(input())
    print (rand)
    if player == 1 :
        print ("gol")
        print ("you win")
    if player == 2 :
        print ("pooch")
        print ("you lose")
if rand == 2 :
    player = int(input())
    print (rand)
    if player == 2 :
        print ("gol")
        print ("you win")
    if player == 1 :
        print ("pooch")
        print ("you lose")
