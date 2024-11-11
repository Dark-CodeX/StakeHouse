import random
import os
import math

def guess(user):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Getting ready, set your initial conditions:")
    max_high = int(input("Enter maximum bound: "))
    num = random.randint(0, max_high)
    points_on_bet = float(input("Amount: "))
    target_multiplier = 1
    if points_on_bet > user.balance:
        print("Amount exceded the available balance")
        return
    while True:
        gss = int(input("Guess the number: "))
        if gss == -1:
            break
        elif gss == num:
            target_multiplier *= max_high // 2
            print(f"Multiplier = {target_multiplier}x")
            print(f"Net Gain: {(target_multiplier * points_on_bet) - points_on_bet}")
        elif gss != num:
            user.balance -= points_on_bet
            print(f"You lost!, new balance = {user.balance}")
            return
        num = random.randint(0, max_high)
    user.balance += (target_multiplier * points_on_bet) - points_on_bet
    print(f"You won!, new balance = {user.balance}")