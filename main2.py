import sys, random
assert sys.version_info >= (3,8), "This script requires at least Python 3.8"

number = random.randrange(1,11)
print(str(number))
guess = input("\nPlease guess a number from 1 to 10: ")
guess = int(guess)
if guess == number:
    print("\nGreat job! You got it!")
    x = input("\nCan you do it again? Yes or No? ")
    if x.lower() == "yes" or x.lower() == "y":
        number2 = random.randrange(1,11)
        print(str(number2))
        guess2 = input("\nPlease guess a number again from 1 to 10: ")
        guess2 = int(guess2)
        if guess2 == number2:
            print("\nGreat job! You got it!")
            y = input("\nCan you go for the Hat trick? Yes or No? ")
            if str(y).lower() == "yes" or str(y).lower() =="y":
                number3 = random.randrange(1,21)
                print(str(number3))
                guess3 = input("\nSince this is for all the marbles, please guess a number between 1 tom 20: ")
                guess3 = int(guess3)
                if guess3 == number3:
                    print("\nWOW! You're really amazing, and don't let anyone else tell you different! Thanks for Playing!\n")
                else:
                    print("\nNormally third time's the charm...")
                    print("\nThe number was " + str(number3))
                    print("\nIt was worth a try! Thanks for playing!" +"\n")
            else: 
                print("\nNormally third time's the charm...")
                print("\nRegardless, Thanks for Playing!" + "\n")
        else:
            print("\nSorry, better luck next time.")
            print("\nThe number was " + str(number2)+"\n")
    else:
        print("\nThere's always time for more later!" + "\n")
else:
    print("\nSorry, better luck next time.")
    print("\nThe number was " + str(number)+"\n")