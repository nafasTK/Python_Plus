signs = {
	"Multiply" : "*" , 
	"divide" : "/" , 
	"plus" : "+" , 
	"minus" : "-" 
}
print (signs)

a = float(input("Please enter your first number: "))
b = float(input("Please enter your second number: "))
c = input("Please enter one of that signs: ")

################################

def my_function(num1, num2) :
	if c == "*" :
		print (num1 * num2)
	elif c == "/" :
		print (num1 / num2)
	elif c == "+" :
		print (num1 + num2)
	elif c == "-" :
		print (num1 - num2)
	else :
		print ("It's wrong") 

my_function (a , b)	