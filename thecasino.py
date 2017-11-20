from random import randint

def guessingGame(balance):
    bet = betty(balance)
    guessesTaken = 1
    number = randint(1, 20)
    print("I am thinking of a number between 1 and 20.")
    while guessesTaken < 5:
        guess = raw_input('Take a guess: ')
        if guess.isdigit():
            guess = int(guess)
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
            print "Your current balance is $",balance
            return balance

def craps(balance):
    bet = betty(balance)
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
        if dsum in [2,3,12]:
            balance = balance - bet
            print "You lost", bet, "dollars. \n Your current balance is $",balance
            return balance
        elif dsum in [7,11]:
            balance = balance + bet
            print "You won", bet, "dollars. \n Your current balance is $",balance
            return balance
        else:
            if tries > 1 and dsum == dsumFirst:
                balance = balance + bet
                print "You won", bet, "dollars. \n Your current balance is $",balance
                return balance
            else:
                print "You didn't win or lose."
                start = raw_input('Press "enter" to roll the dice: ')
                die1 = randint(1,6)
                die2 = randint(1,6)
                dsum = die1 + die2
                tries += 1

def inBetween(balance):
    print "Coming Soon"
    cards = {Ace: 1, Two: 2, Three: 3, Four: 4, Five: 5, Six: 6, Seven: 7, Eight: 8, Nine: 9, Ten: 10, Jack: 11, Queen: 12, King: 13}
    card1 = random.choice(cards)
    card2 = random.choice(cards)
    print card1, card2
def directions():
    print "\n HOW TO PLAY: \n"
    print "GUESSING GAME: \n You are to guess a number between 1 and 20. You will continue to guess to you reach the number. Your pay out is determined by how many tries you take to guess the number.\n"
    print "CRAPS: \n You will roll two die. If the sum of both die is 2, 3, or 12, you lose. If the sum is 7 or 11 you win. After the first roll, if at any time the sum of the die is equal to the sum that you got on the first roll, you win.\n"
    print "IN BETWEEN: \n Coming Soon!\n"

def betty(balance):
    validBet = 0
    while validBet == 0:
        print "You have $", balance
        bet = raw_input("Enter a bet: ")
        if bet.isdigit():
            bet = int(bet)
            if bet <= balance and bet > 0:
                if bet == 666:
                    print "Just when you think its over. Your Demons laugh and whisper. /\/\(=-=)/\/\ "
                return bet
        else:
            print "That is not a valed bet."

def main():
    balance = 1000
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
