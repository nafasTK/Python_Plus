import random
import string


lower = string.ascii_lowercase
uppper = string.ascii_uppercase
symbols = "!@#$%^&/*-+[]"
numbers = "0123456789"
all = lower + uppper + symbols + numbers


while True:

    choise = input("\nchoose an option :\n1) create a password\n2) Check your information\n3) exit\nyour choice : ")

    if choise == "1" :
        name = input("please enter your name : ")
        last_name = input("please enter your last name : ")
        program = input("which program do you want to set a password for ? ")
        acount = input(f"enter your {program} user name : ")
        discription = input("you can enter the discription : ")
        length = int(input("enter the password length : "))
        password = "".join(random.sample(all, length))
        print(f"your password : {password}")
        

        with open("passwords.txt", "a") as file :
            file.write(f"1- Name : {name} {last_name}\n2- Program : {program}\n3- User name : {acount}\n4- Discription : {discription}\n5- Password : {password}\n")
            file.write("-" * 45)
            file.write(" ")
    elif choise == "2" :
        with open("passwords.txt", "r") as file :
            read = file.read()
            print (" ")
            print (read)

    elif choise == "3" :
        break

    else:
        print("invalid option")

        

end = input(" ")