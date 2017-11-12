
import random
def guessingGame(balance):
    # This is a guess the number game.
     import random

     guessesTaken = 0

     number = random.randint(1, 20)
     print("I am thinking of a number between 1 and 20.")

     while guessesTaken < 6:
         print('Take a guess.')
         guess = input()
         guess = int(guess)

         guessesTaken = guessesTaken + 1

         if guess < number:
             print('Your guess is too low.')

         if guess > number:
             print('Your guess is too high.')

         if guess == number:
             break

     if guess == number:
         guessesTaken = str(guessesTaken)
         print('Good job, You guessed my number in ' + guessesTaken + ' guesses!')

     if guess != number:
         number = str(number)
         print('Nope. The number I was thinking of was ' + number)




def craps(balance):
    x = raw_input(' press "enter" to roll the dice')
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    dsum = die1 + die2
    print "You rolled", dsum


    if dsum == 2 or dsum ==3 or dsum == 12:
        game = "you lose"

    elif dsum == 7 or dsum == 11:
        game = "you win"

    else:

        game = True
        x = raw_input('')
        while game:
    		die1 = random.randint(1,6)
    		die2 = random.randint(1,6)
    		dsum2 = die1 + die2

    		print "You rolled", dsum2
    		x = raw_input("")

    		if dsum2 == dsum:
    	           print "you win"

    		elif dsum2 == 7:
    	           print "you lose"
    return balance




def inBetween(balance):
    print("Coming Soon")


def directions():
    print "\nGAMES: \n 1 - Guessing Game \n 2 - Craps \n 3 - In Between \n 4 - Help \n 5 - Quit"
    print "HOW TO PLAY: \n \nGUESSING GAME: \nThe goal of the Guessing Game is pretty simple. You are to guess a number between 1 and 20. You will continue to \nguess to you reach the number. Your pay out is determined by how many tries you take to guess the number.\n"
    print "CRAPS: \n Coming Soon!\n"
    print "IN BETWEEN: \n Coming Soon!\n"


def main():
    balance = "100"
    print "Welcome to the Python casino! What would you like to do?"
    choice = "0"
    while choice != "5":
        choice = raw_input("\n 1 - Guessing Game \n 2 - Craps \n 3 - In Between \n 4 - Help \n 5 - Quit \nEnter 1-5 to choose what you want to do: ")
        if choice == "1":
            balance = guessingGame(balance)
        elif choice == "2":
            balance = craps(balance)
        elif choice == "3":
            balance = inBetween(balance)
        elif choice == "4":
            help()

main()
