def welcomeScreen():
    print("+---------------------+")
    print("| WELCOME TO J&C BANK |")
    print("|---------------------|")
    print("| Author: Christopher |")
    print("| Date: 14/06/2023    |")
    print("|                     |")
    print("|    --MAIN MENU--    |")
    print("|  1) ADMIN LOGIN     |")
    print("|  2) USER LOGIN      |")
    print("|  3) HELP            |")
    print("|  4) EXIT            |")
    print("+---------------------+")
    choice = int(input("SELECT: "))
    return choice

def adminLogin():
    print()
    print("PLEASE LOGIN")
    tmpID = input("Admin ID: ")
    tmpPass = input("Password: ")

    if tmpID == "1" and tmpPass == "1":
        return 1
    else:
        return 0

def userLogin():
    print()
    print("PLEASE LOGIN")
    tmpNum = input("Account Number: ")
    tmpPin = input("Pin: ")
    #not complete

def help():
    print()
    print("J&C Bank is a simple banking program developed")
    print("to show the working of a realtime\nbank")
