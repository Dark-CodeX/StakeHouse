import os
import random

FILE_PATH = "./user.cnf"

def create_user():
    name = input("Enter your name: ")
    balance = 500
    wager = 0
    srand = random.randint(1000000, 9999999) * random.randint(1000000, 9999999)
    save = open(FILE_PATH, "w")
    save.write(name + "\n" + str(balance) + "\n" + str(wager) + "\n" + str(srand) + "\n")
    save.close()

if __name__ == "__main__":
    if os.path.exists(FILE_PATH) == False:
        create_user()
    else:
        user = open(FILE_PATH, "r")
        user_content = user.readlines()
        user.close()
        print("Welcome to StakeHouse, dear", user_content[0], end="")
        print("Your current points are:", user_content[1], end="")
        print("Select the game you wanna play?")
        print("\t1. Mines")
        print("\t2. ")
        option = input("Your choice? ")