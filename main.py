import user.user as stakehouse_user
import games.limbo as stakehouse_limbo

FILE_PATH = "./user.cnf"

if __name__ == "__main__":
    user = stakehouse_user.user()
    user.open(FILE_PATH)
    print("Welcome to StakeHouse, dear", user.name, end="")
    while True:
        print("Your current points are:", user.balance)
        print("Select the game you wanna play?")
        print("\t1. Mines")
        print("\t2. Limbo")
        print("\t0: Exit")
        game_option = int(input("Your choice? "))
        if game_option == 1:
            pass
        elif game_option == 2:
            stakehouse_limbo.limbo(user)
        elif game_option == 0:
            break
        else:
            print("Invalid choice")
                