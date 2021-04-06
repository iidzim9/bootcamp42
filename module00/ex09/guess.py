import random

print("This is an interactive guessing game!\nYou have to enter a number between 1 and 99 to find out the secret number.\nType 'exit' to end the game.\nGood luck!")
n = random.randint(0,99)
print(n)
cpt = 0
while True:
    nbr = input("What's your guess between 1 and 99?\n>> ")
    cpt += 1
    if nbr.isdecimal():
        x = int(nbr)
        if n > x:
            print("Too low!")
        elif n < x:
            print("Too high!")
        elif n == 42 and cpt == 0:
            print("The answer to the ultimate question of life, the universe and everything is 42.'nCongratulations! You got it on your first try!")
        else:
            print("Congratulations, ", end = "")
            if cpt == 0:
                print("You got it on your first try!")
            else:
                print("you've got it!")
                print("You won in %d attempts!" % cpt)
            break
    elif nbr == "exit":
        print("Goodbye!")
        exit()
    else:
        print("That's not a number.")