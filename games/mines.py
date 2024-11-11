import random
import os

def print_matrix(matrix, opened):
    print("     1     2     3     4     5   ")
    print("  +-----+-----+-----+-----+-----+")
    for i in range(5):
        print(f"{i + 1} |", end="")
        for j in range(5):
            if matrix[j][i] == True:
                print(f"  {"💣" if (j, i) in opened else "? "}", "|" if j <= 3 else "" ,end="")
            else:
                print(f"  {"💎" if (j, i) in opened else "? "}", "|" if j <= 3 else "" ,end="")
        print("|\n", end="")
        print("  +-----+-----+-----+-----+-----+")

def is_between(num, low, high):
    return (low <= num <= high)

def create_matrix(mines):
    mat = []
    for i in range(mines):
        mat.append(True) # mine
    for i in range(25 - mines):
        mat.append(False) # not mine

    random.shuffle(mat)
    return [mat[i * 5:(i + 1) * 5] for i in range(5)]

def mines(user):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Getting ready, set your initial conditions:")
    no_of_mines = int(input("Number of mines: "))
    if not is_between(no_of_mines, 1, 24):
        print("Mines count must be in range of [1, 24], try another")
        return
    points_on_bet = float(input("Amount: "))
    if points_on_bet > user.balance:
        print("Amount exceded the available balance")
        return
    matrix = create_matrix(no_of_mines)
    opened = []
    print_matrix(matrix, [])
    while len(opened) <= 25:
        op = input("Which slot you wanna open? [CR]: ")
        if(op == "-1"):
            multiplier =( len(opened) / (25 - no_of_mines) * (25 - 1) )+ 1
            print(f"Multiplier = {multiplier}x\nNet Gain = {(multiplier * points_on_bet) - points_on_bet}")
            break
        col = int(op[0]) - 1
        row = int(op[1]) - 1
        if not is_between(col, 0, 5):
            print("Column must be in range of [1, 5], try another")
            continue
        if not is_between(row, 0, 5):
            print("Row must be in range of [1, 5], try another")
            continue
        if (col, row) in opened:
            print("That slot is already opened, try another")
            continue
        opened.append((col, row))
        if matrix[col][row] == True:
            print_matrix(matrix, opened)
            user.balance -= points_on_bet
            print(f"You lost!, new balance = {user.balance}")
            return
        else:
            print_matrix(matrix, opened)
            multiplier =( len(opened) / (25 - no_of_mines) * (25 - 1) )+ 1
            print(f"Multiplier = {multiplier}x\nNet Gain = {(multiplier * points_on_bet) - points_on_bet}")
    user.balance += (multiplier * points_on_bet) - points_on_bet
    print(f"You won!, new balance = {user.balance}")
