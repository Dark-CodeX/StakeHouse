import os
import random

class user():
    def __init__(self):
        self.name = ""
        self.balance = 0

    def create_user(self, location):
        name = input("Enter your name: ")
        balance = 500
        save = open(location, "w")
        save.write(name + "\n" + str(balance) + "\n")
        save.close()

    def open(self, location):
        if os.path.exists(location) == False:
            self.create_user(location)
        user = open(location, "r")
        user_content = user.readlines()
        user.close()
        self.name = user_content[0]
        self.balance = float(user_content[1])

    def write(self, location):
        save = open(location, "w")
        save.write(self.name + str(self.balance) + "\n")
        save.close()