import random as rd


def start():
    print("PLEASE SELECT THE LEVEL\n")

    print("PRESS 1 FOR LEVEL->1\nPRESS 2 FOR LEVEL->2\nPRESS 3 FOR LEVEL->3\n")
    num = int(input("ENTER YOUR CHOICE : "))

    if num == 1:
        print("\nWELCOME TO LEVEL 1\n")

        print("\nYOU HAVE 3 LIVES FOR GUESSING THE NUMBER\n")

        print("\nLET'S START THE GAME\n")

        print("GUESS THE NUMBER BETWEEN 1 TO 5")

        x = rd.randint(1, 5)
        process(x)




    elif num == 2:
        print("\nWELCOME TO LEVEL 2\n")

        print("YOU HAVE 3 LIVES FOR GUESSING THE NUMBER\n")

        print("\nLET'S START THE GAME\n")

        print("GUESS THE NUMBER BETWEEN 1 TO 15")

        x = rd.randint(1, 15)
        process(x)

    elif num == 3:
        print("\nWELCOME TO LEVEL 3\n")

        print("\nYOU HAVE 3 LIVES FOR GUESSING THE NUMBER\n")

        print("\nLET'S START THE GAME\n")

        print("GUESS THE NUMBER BETWEEN 1 TO 30")

        x = rd.randint(1, 30)
        process(x)

    else:
        print("\nYOU HAVE ENTER WRONG LEVEL\n")
        print("WELCOME TO THE DEFAULT LEVEL : LEVEL 2\n")
        print("\nYOU HAVE 3 LIVES FOR GUESSING THE NUMBER\n")

        print("\nLET'S START THE GAME\n")

        print("GUESS THE NUMBER BETWEEN 1 TO 15")

        x = rd.randint(1, 15)
        process(x)


def process(x):

    for i in range(1,4):
        a = int(input("\n  ENTER YOUR GUESS NUMBER {} : ".format(i)))
        if a == x:
            print("\n YOU GUESSED CORRECTLY ")
            print("\n$$$$ YOU WIN THE GAME $$$$\n")
            re = input("DO YOU WANT TO PLAY AGAIN (y/n) : ")
            print()
            if re == 'y' or re == 'Y':
                start()
            else:
                print("\n THANK YOU FOR PLAYING THE GAME\n")
                break
        else:
            print("\nYOUR GUESS IS WRONG. PLEASE TRY AGAIN\n")
            print("{} LIVES ARE REMAINED".format(3-i))
            if 3-i == 0:
                print("\nYOU LOSE THE GAME\n")

                print("THE NUMBER IS {} ".format(x))

                print("GAME OVER\n")

                re = input("DO YOU WANT TO PLAY AGAIN (y/n) : ")
                print()
                if re == 'y' or re == 'Y':
                    start()
                else:
                    break


if __name__ == "__main__":
    print("\n\nWELCOME TO THE NUMBER GUESSING GAME\n ")
    start()
