ice_cream_list = {
    "Vanilla": 3,
    "Chocolate" : 4,
    "Soffron" : 5,
    "Coffee": 4,
    "Strawberry": 3,
    "Nutella": 5,
    "Banana" : 3 
}
for ice_cream in ice_cream_list :
    print (ice_cream)
a = True
coast_1 = 0
coast_2 = 0
coast_3 = 0
coast_4 = 0
coast_5 = 0
coast_6 = 0
coast_7 = 0

print ("if you dont want any  bread enter 'no' ")
while a :
    coastumer = input("which one do you want ? ")
    if coastumer == "Vanilla" :
        mach = int(input("how many scoops of Vanilla ice cream would you like ? "))
        coast_1 = mach * 3
    elif coastumer == "Chocolate" :
        mach = int(input("how many scoops of Chocolate ice cream would you like ? "))
        coast_2 = mach * 4
    elif coastumer == "Soffron" :
        mach = int(input("how many scoops of Soffron ice cream would you like ? "))
        coast_3 = mach * 5
    elif coastumer == "Coffee" :
        mach = int(input("how many scoops of Coffee ice cream would you like ? "))
        coast_4 = mach * 4
    elif coastumer == "Strawberry" :
        mach = int(input("how many scoops of Strawberry ice cream would you like ? "))
        coast_5 = mach * 3
    elif coastumer == "Nutella" :
        mach = int(input("how many scoops of Nutella ice cream would you like ? "))
        coast_6 = mach * 5
    elif coastumer == "Banana" :
        mach = int(input("how many scoops of Banana ice cream would you like ? "))
        coast_7 = mach * 3
    elif coastumer == "no" :
        print ("OK")
        break
    else :
        print ("it's wrong")
    total = coast_1 + coast_2 + coast_3 + coast_4 + coast_5 + coast_6 + coast_7

##################################################################

print (" ")

dishes = input("bowl or cone ? ")

if dishes == "cone" :
    total = total + 1
    print ("OK")
    print (" ")
elif dishes == "bowl" :
    total = total + 1
    print ("OK")
    print (" ")
else :
    print ("it's wrong")
    b = True
    while b == True :
        dishes = input("bowl or cone ? ")
        if dishes == "cone" :
            total = total + 1
            print ("OK")
            print (" ")
            b = False
            break
        elif dishes == "bowl" :
            total = total + 1
            print ("OK")
            print (" ")
            b = False
            break
        else :
            print ("it's wrong")
            b = True

##################################################################

sprinkles = input("Do you want sprinkles ? ")
if sprinkles == "yes" :
    print ("OK")
    print (" ")
    ice_cream_list = {
        "Vanilla sprinkle": 1,
        "Chocolate sprinkle" : 1,
        "Soffron sprinkle" : 1,
        "Coffee sprinkle": 1,
        "Strawberry sprinkle" : 1,
        "Nutella sprinkle" : 1,
        "Banana sprinkle" : 1,
    }
    for ice_cream in ice_cream_list :
        print (ice_cream)
    which_sprinkle = input("which sprinkles do you want ? ")
    if which_sprinkle == "Vanilla sprinkle" or "Chocolate sprinkle" or "Soffron sprinkle" or "Strawberry sprinkle" or "Nutella sprinkle" or "Banana sprinkle" :
        total = total + 1

elif sprinkles == "no" :
    print ("OK")
    print (" ")
    
else :
    print ("it's wrong")
    b = True
    while b == True :
        sprinkles = input("Do you want sprinkles ? ")
        if sprinkles == "yes" :
            ice_cream_list = {
                "Vanilla sprinkle": 1,
                "Chocolate sprinkle" : 1,
                "Soffron sprinkle" : 1,
                "Coffee sprinkle": 1,
                "Strawberry sprinkle" : 1,
                "Nutella sprinkle" : 1,
                "Banana sprinkle" : 1,
            }
            which_sprinkle = input("which sprinkles do you want ? ")
            if which_sprinkle == "Vanilla sprinkle" or "Chocolate sprinkle" or "Soffron sprinkle" or "Strawberry sprinkle" or "Nutella sprinkle" or "Banana sprinkle" :
                total = total + 1

        elif sprinkles == "no" :
                print ("OK")
                b = False
                break

        else :
            print ("it's wrong")
            b = True

##################################################################

print (f"you should pay {total}$")

input()
