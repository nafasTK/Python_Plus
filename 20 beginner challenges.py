import random
import time
import string

#####################__1st__#####################

print ("-"*120, "\nHello World:")
print ("Hello, World!")

#####################__2nd__#####################

print("-"*120, "\nOdd or Even:")
a = True

while a == True :
    try:
        numb1 = int(input("enter a number: "))
        a = False
    except ValueError:
        print ("Only numbers are allowed!!")
if numb1/2 == numb1//2:
    print (f"{numb1} is even.")
if numb1/2 != numb1//2:
    print (f"{numb1} is odd.")

#####################__3rd__#####################

print("-"*120, "\nCalculator:")
signs = {
	"Multiply" : "*", 
	"divide" : "/", 
	"plus" : "+", 
	"minus" : "-" 
}
for i in signs :
    print (i,f" :  {signs[i]}")

a = True
while a == True :
    try:
        numb2 = float(input("Please enter your first number: "))
        a = False
    except ValueError:
        print ("Only numbers are allowed!!")

sign = input("Please enter one of that signs: ")

b = True
while b == True :
    try:
        numb3 = float(input("Please enter your second number: "))
        b = False
    except ValueError:
        print ("Only numbers are allowed!!")

def my_function(num1, num2) :
	if sign == "*" :
		print (num1 * num2)
	elif sign == "/" :
		print (num1 / num2)
	elif sign == "+" :
		print (num1 + num2)
	elif sign == "-" :
		print (num1 - num2)
	else :
		print ("It's wrong") 

my_function (numb2, numb3)

#####################__4th__#####################

print("-"*120, "\nFibonacci Sequence:")
a = True
first = 0
second = 1
m = 2
fibonacci_list = [0, 1]

while a == True :
    try:
        numb4 = int(input("How many numbers of Fibonacci Sequence do you want? "))
        if numb4<2:
            print("the number can't be less than 2!")
            a = True
        else:
            a = False
    except ValueError:
        print ("Only numbers are allowed!!")

for i in range(numb4-1):
    third = first + second
    fibonacci_list.insert(m, third)
    m = m + 1
    first = second
    second = third
    
print(fibonacci_list)

#####################__5th__#####################

print("-"*120, "\nFactorial Finder:")
nums_list = []
n = 1
a = True
while a == True :
    try:
        numb5 = int(input("What number do you want the factorial of? "))
        a = False
    except ValueError:
        print ("Only numbers are allowed!!")

for i in range(numb5):
    nums_list.append(i+1)
for p in range(numb5-1):
    n = n * nums_list[p+1]

print(f"{numb5}! = {n}")

#####################__6th__#####################

print("-"*120, "\nNumber Guessing Game:")
computer_choice = random.randint(1,5)

a = True
while a == True :
    try:
        numb6 = int(input("The computer has chosen a number between 1 and 5, and you have to guess what it is.\nEnter your guess: "))
        a = False
    except ValueError:
        print ("Only numbers are allowed!!")
print(f"The computer choise: {computer_choice}")

if numb6 == computer_choice:
     print("U Won!!")
else :
     print("You lost...")

#####################__7th__#####################

print("-"*120, "\nPalindrome Checker:")

numb7 = (input("enter a your string: "))

cleaned_string = ''.join(numb7.split()).lower() # With the help of ChatGPT(just this line)
reversed_string = cleaned_string[::-1]

if cleaned_string == reversed_string :
    print (f"{numb7} is a palindrome ✔️")
else:
     print (f"{numb7} is not a palindrome ❌")

#####################__8th__#####################

print("-"*120, "\nCountdown Timer:")
a = True
while a == True :
    try:
        numb8 = int(input("How many seconds do you want to count down? "))
        a = False
    except ValueError:
        print ("Only numbers are allowed!!")
for i in range(numb8+1):
    print (numb8)
    time.sleep(1)
    numb8 = numb8 - 1

#####################__9th__#####################

print("-"*120, "\nMultiplication Table:")
a = True
while a == True :
    try:
        numb9 = int(input("Enter a number to generate its multiplication table from 1 to 10: "))
        a = False
    except ValueError:
        print ("Only numbers are allowed!!")

print(f"Multiplication Table for {numb9}:")
for i in range(10):
    result = numb9 * (i+1)
    print(f"{numb9} x {i+1} = {result}")

#####################__10th__#####################

print("-"*120, "\nSimple Quiz:")
questions = {
    "A) 2 x 6 : \n1)20       2)12        3)24       4)26" : 2 ,
    "B) 8 x 5 : \n1)56       2)80        3)40       4)20" : 3 ,
    "C) 3 x 7 : \n1)21       2)27        3)36       4)14" : 1 
}
score = 0
keys = list(questions.keys())
for i in range(3):
    x = keys[i]
    a = True
    while a == True :
        try:
            answer = int(input(f"\n{x}\nyour answer : "))
            a = False
        except ValueError:
            print ("Only numbers are allowed!!")
    if questions[x] == answer:
        score = score + 1
    else:
        score = score
print (f"Score: {score} out of 3")

#####################__11th__#####################

print("-"*120, "\nPassword Generator:")
lower = string.ascii_lowercase
uppper = string.ascii_uppercase
numbers = "0123456789"
all = lower + uppper + numbers
length = random.randint(5,7)
password = "".join(random.sample(all, length))
print(f"password : {password}")

#####################__12th__#####################

print("-"*120, "\nFind the Largest Number:")
numb_list = []
for i in range(10):
    numb_list.insert(i, random.randint(-100, 100))
print(numb_list)
numb_list.sort()
print(numb_list)
print (f"The largest number: {numb_list[9]}")

#####################__13th__#####################

print("-"*120, "\nRock, Paper, Scissors Game:")
print("rock\npaper\nscissors")
randomNumber = random.randint(0,2)
computerMove = ""

if randomNumber == 0:
    computerMove = "rock"
elif randomNumber == 1:
    computerMove = "paper"
elif randomNumber == 2:
    computerMove = "scissors"
while True:
    player1 = input("make your move : ")
    if player1 == "rock" or player1 == "paper" or player1 == "scissors":
        break
    else:
        print("Invalid !!")
print(f"computer move : {computerMove}")
player2 = computerMove

if player1 == "rock" and player2 == "scissors":
    print ("u won !")
elif player1 == "rock" and player2 == "paper":
    print("computer won !")
elif player1 == "paper" and player2 == "rock":
    print ("u won !")
elif player1 == "paper" and player2 == "scissors":
    print("computer won !")
elif player1 == "scissors" and player2 == "paper":
    print ("u won !")
elif player1 == "scissors" and player2 == "rock":
    print("computer won !")
elif player1 == player2:
        print ("thats a tie !")

#####################__14th__#####################

print("-"*120, "\nConvert Celsius to Fahrenheit:")
a = True
while a == True :
    try:
        c = float(input("Enter the Celsius to turn it to Fahrenheit: "))
        a = False
    except ValueError:
        print ("Only numbers are allowed!!")
f = (c * 1.8) + 32
print (f"{c}C = {f}F")

print("\nConvert Fahrenheit to Celsius:")
a = True
while a == True :
    try:
        f = float(input("Enter the Fahrenheit to turn it to Celsius: "))
        a = False
    except ValueError:
        print ("Only numbers are allowed!!")
c = (f / 1.8) - 32
print (f"{f}F = {c}C")

#####################__15th__#####################

print("-"*120, "\nBasic To-Do List:")

#####################__16th__#####################

print("-"*120, "\nEven Number List Filter:")
nums = []
even_nums = []
odd_nums = []
a = True
while a == True :
    try:
        num_numbers = int(input("How many numbers do you want to enter: "))
        a = False
    except ValueError:
        print ("Only numbers are allowed!!")
for i in range(num_numbers):
    a = True
    while a == True :
        try:
            number = int(input(f"Enter number {i + 1}: "))
            a = False
        except ValueError:
            print ("Only numbers are allowed!!")
    nums.append(number)
    if nums[i]/2 == nums[i]//2 :
        even_nums.append(nums[i])
    else :
        odd_nums.append(nums[i])
print (f"Odd numbers: {odd_nums}\nEven numbers: {even_nums}")

#####################__17th__#####################

print("-"*120, "\nSum of Digits:")
sum_of_digits = 0
a = True
while a == True :
    try:
        numb10 = int(input("Enter number: "))
        a = False
    except ValueError:
        print ("Only numbers are allowed!!")
number_str = str(numb10)
digits = []
n = 0

for digit in number_str:
    digits.append(int(digit))
    sum_of_digits = sum_of_digits + digits[n]
    n += 1
print (f"Sum of Digits: {sum_of_digits}")

#####################__18th__#####################

print("-"*120, "\n:Word Counter")
sentence = input("Enter your sentence: ")
word_count = 0
words = sentence.split()

for word in words:
    word_count += 1
print(f"Number of the words: {word_count}")

#####################__19th__#####################

print("-"*120, "\nSimple Alarm Clock:")
a = True
while a == True :
    try:
        numb11 = int(input("how many seconds do you want to wait for? "))
        a = False
    except ValueError:
        print ("Only numbers are allowed!!")
time.sleep(numb11)
print ("time's up!")

#####################__20th__#####################

print("-"*120, "\nDice Roll Simulato:")
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
print (f"First Dice: {dice1}\nSecond Dice: {dice2}")
