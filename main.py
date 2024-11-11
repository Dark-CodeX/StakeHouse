import user.user as stakehouse_user
import games.limbo as stakehouse_limbo
import games.mines as stakehouse_mines
import games.guess as stakehouse_guess

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
        print("\t3. Guess")
        print("\t0: Exit")
        game_option = int(input("Your choice? "))
        if game_option == 1:
            stakehouse_mines.mines(user)
            user.write(FILE_PATH)
        elif game_option == 2:
            stakehouse_limbo.limbo(user)
            user.write(FILE_PATH)
        elif game_option == 3:
            stakehouse_guess.guess(user)
            user.write(FILE_PATH)
        elif game_option == 0:
            user.write(FILE_PATH)
            break
        else:
            print("Invalid choice")
                