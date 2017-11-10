def main():
    balance = 100
    print "Welcome to the Python casino! What would you like to do?"
    print "\n 1 - Guessing Game \n 2 - Craps \n 3 - In Between \n 4 - Directions \n 5 - Quit"
    choice = 0
    while choice != 5
        choice = input("Enter 1-5 to choose what you want to do: ")
        if choice = 1:
            balance = guessingGame(balance)
        elif choice = 2:
            balance = craps(balance)
        elif choice = 3:
            balance = inBetween(balance)
        elif choice = 4:
            directions()
main()

