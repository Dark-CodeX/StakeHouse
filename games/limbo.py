import os
import random

def limbo(user):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Getting ready, set your initial conditions:")
    target_multiplier = float(input("Target Multiplier: "))
    points_on_bet = float(input("Amount: "))
    print("Your win chance % is:", (1/ target_multiplier )* 100)
    print("Net gain on win:", (points_on_bet * target_multiplier) - points_on_bet)

    while(user.balance >= points_on_bet):
        play = input("Select:\n\t1. Play(default)\n\t2. Change conditions\n\t3. Quit\n?")
        play = 1 if play == "" else int(play)
        if play == 1:
            random_num = random.randint(0, int(target_multiplier) * 2)
            print(f"RESULT = {random_num}%")
            if(random_num > target_multiplier):
                user.balance -= points_on_bet
                print(f"You lost!, new balance = {user.balance}")
            else:
                user.balance += (points_on_bet * target_multiplier) - points_on_bet
                print(f"You won!, new balance = {user.balance}")
        elif play == 2:
            target_multiplier = float(input("Target Multiplier: "))
            points_on_bet = float(input("Amount: "))
            print("Your win chance % is:", (1/ target_multiplier )* 100)
            print("Net gain on win:", (points_on_bet * target_multiplier) - points_on_bet)
        elif play == 3:
            break
    os.system('cls' if os.name == 'nt' else 'clear')
    
    