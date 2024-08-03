###### welcome ######

y = 0
z = 0
total_1 = 0
total_2 = 0
a = True
print ("Hello , welcome to the elevator")
print ("This elevator just has two buttons , up & down")
print (" ")

####### name #######

first = input("please enter your name : ")
second = input("please enter your name : ")
print ("OK")

print ("u : up")
print ("d : down")
print (" ")

###### Floor selection ######

while a == True :
	floor = input("{} , where do you want to go ? (u/d) ".format(first))
	if floor == "u" :
		total_1 = total_1 + 1
		y = y + 1
	elif floor == "d" :
		total_1 = total_1 - 1
		y = y + 1
	else :
		print ("it's wrong")
		a = True

	if y == 4 :
			break


print (f"{first} wants to go to {total_1} floor")

total = total_1 + total_2
						
while a == True :
		
	floor = input("{} , where do you want to go ? (u/d) ".format(second))
	if floor == "u" :
		total_2 = total_2 + 1
		z = z + 1
		total = total_1 + total_2
	elif floor == "d" :
		if total == -4 :
			print ("There are only 4 floors underground")
			a = True
		else :
			total_2 = total_2 - 1
			total = total_1 + total_2
			z = z + 1
	else :
		print ("it's wrong")
		a = True
	
	if z == 4 :
		break
		
			
print (f"{second} wants to go to {total_2} floor")
total = total_1 + total_2

print (f"Finally , you're on {total} floor")

s = input(" ")