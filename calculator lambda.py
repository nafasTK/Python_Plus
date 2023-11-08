signs = {
	"Multiply" : "*" , 
	"divide" : "/" , 
	"plus" : "+" , 
	"minus" : "-" 
}
print (signs)

a=float(input("please enter first number: "))
b=float(input("please enter second number: "))
oprator=str(input("please enter oprator: "))
num1=lambda a,b : a+b
num2=lambda a,b : a-b
num3=lambda a,b : a*b
num2=lambda a,b : a/b

################################

if oprator=="+":
    print(num1(a,b))
elif oprator=="-":
    print(num2(a,b))
elif oprator=="*":
    print(num3(a,b))
elif oprator=="/":
    print(num4(a,b))
more=str(input("do you want to add new number?y/n "))

while more=="y":
    num1=int(input("please enter first number: "))
    num2=int(input("please enter second number: "))
    oprator=str(input("please enter oprator: "))
    if oprator=="+":
        print(num1(a,b))
    elif oprator=="-":
        print(num2(a,b))
    elif oprator=="*":
        print(num3(a,b))
    elif oprator=="/":
        print(num4(a,b))
    more=str(input("do you want to add new number?y/n "))
    if more=="n":
        break