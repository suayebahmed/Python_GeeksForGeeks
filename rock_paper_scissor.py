a = input("Name of player A: ")
b = input("Name of player B: ")
print("")
print("If you're ready for the game, then select your choice: ")
print("")
user_a = input(f"insert your choice {a}: (r)ock, (p)aper, or (s)cissor=> ")
user_b = input(f"insert your choice {b}: (r)ock, (p)aper, or (s)cissor=> ")
game = False

while True:
    if user_a == user_b:
        print("You're tie.")
    elif user_a == "r":
        if user_b == "p":
            print(f"{user_b} won the game")
        elif user_b == "s":
            print(f"{user_a} won the game")
        
    elif user_a == "p":
        if user_b == "r":
            print(f"{user_a} won the game")
        elif user_b == "s":
            print(f"{user_b} won the game")

    elif user_a == "s":
        if user_b == "p":
            print(f"{user_a} won the game")
        elif user_b == "r":
            print(f"{user_b} won the game")

    else:
        print("You've put a invalid syntax. Only enter 'r', 'p', or 's'")

    break   
