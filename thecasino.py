from random import randint

def guessingGame(balance):
    bet = input("Enter how much money you want to bet from $1 - $" + str(balance) + ": ")
    guessesTaken = 1
    number = randint(1, 20)
    print("I am thinking of a number between 1 and 20.")
    while guessesTaken < 5:
        guess = input('Take a guess: ')
        if guess < number:
            print('Your guess is too low.')
        if guess > number:
            print('Your guess is too high.')
        if guess == number:
            guessesTaken = str(guessesTaken)
            print('Good job, you guessed my number in ' + guessesTaken + ' guesses!')
            print "You won", bet, "dollars."
            balance = balance + bet
            print "Your current balance is", balance
            return balance
        guessesTaken = guessesTaken + 1
    if guessesTaken == 5:
        print "The number was", number
        print "You lost", bet, "dollars."
        balance = balance - bet
        print "Your current balance is", balance
        return balance

def craps(balance):
    bet = input("Enter how much money you want to bet from $1 - $" + str(balance) + ": ")
    start = raw_input('Press "enter" to roll the dice: ')
    die1 = randint(1,6)
    die2 = randint(1,6)
    dsum = die1 + die2
    dsumFirst = dsum
    running = True
    tries = 1
    while running:
        print "First is", dsumFirst
        print "You rolled", dsum
        if dsum != 2 and 3 and 12 and 7 and 11:
            if tries > 1 and dsum == dsumFirst:
                balance = balance + bet
                print "You won", bet, "dollars. \n Your current balance is", balance
                return balance
            else:
                print "You didn't win or lose."
                start = raw_input('Press "enter" to roll the dice: ')
                die1 = randint(1,6)
                die2 = randint(1,6)
                dsum = die1 + die2
                tries += 1
        elif dsum != 2 and 3 and 12:
            balance = balance + bet
            print "You won", bet, "dollars. \n Your current balance is", balance
            return balance
        else:
            balance = balance - bet
            print "You lost", bet, "dollars. \n Your current balance is", balance
            return balance

def inBetween(balance):
    print("Coming Soon")

def directions():
    print "\nGAMES: \n 1 - Guessing Game \n 2 - Craps \n 3 - In Between \n 4 - Help \n 5 - Quit"
    print "\n HOW TO PLAY: "
    print "GUESSING GAME: \n The goal of the Guessing Game is pretty simple. You are to guess a number between 1 and 20. You will continue to \nguess to you reach the number. Your pay out is determined by how many tries you take to guess the number.\n"
    print "CRAPS: \n Coming Soon!\n"
    print "IN BETWEEN: \n Coming Soon!\n"

def main():
    balance = 100
    print "Welcome to the Python casino! What would you like to do?"
    choice = "0"
    while choice != "5":
        if balance == 0:
            print "You lost all your money."
            return
        choice = raw_input("\n 1 - Guessing Game \n 2 - Craps \n 3 - In Between \n 4 - Help \n 5 - Quit \n \n Enter 1-5 to choose what you want to do: ")
        if choice == "1":
            balance = guessingGame(balance)
        elif choice == "2":
            balance = craps(balance)
        elif choice == "3":
            balance = inBetween(balance)
        elif choice == "4":
            directions()
        elif choice == "5":
            print "Your final balance is", balance
            return

main()
