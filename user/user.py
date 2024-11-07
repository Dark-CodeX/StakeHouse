import os
import random

class user():
    def __init__(self):
        self.name = ""
        self.balance = 0
        self.wager = 0
        self.srand = 0

    def create_user(self, location):
        name = input("Enter your name: ")
        balance = 500
        wager = 0
        srand = random.randint(1000000, 9999999) * random.randint(1000000, 9999999)
        save = open(location, "w")
        save.write(name + "\n" + str(balance) + "\n" + str(wager) + "\n" + str(srand) + "\n")
        save.close()

    def open(self, location):
        if os.path.exists(location) == False:
            self.create_user(location)
        user = open(location, "r")
        user_content = user.readlines()
        user.close()
        self.name = user_content[0]
        self.balance = int(user_content[1])
        self.wager = int(user_content[2])
        self.srand = int(user_content[3])

    def write(self, location):
        save = open(location, "w")
        save.write(self.name + "\n" + str(self.balance) + "\n" + str(self.wager) + "\n" + str(self.srand) + "\n")
        save.close()