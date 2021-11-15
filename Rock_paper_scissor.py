# Rock Paper and Scissor Program
import random

game = True
winCount = 0
loseCount = 0
drawCount = 0

# Returns the choice of the user
def UserChoice(choiceNumber):
    if choiceNumber == 1:
        return 'Player chooses Rock'
    elif choiceNumber == 2:
        return 'Player chooses Paper'
    elif choiceNumber == 3:
        return 'Player chooses Scissors'

while game == True:

    # Asks option from user and generates a random number
    userChoice = int(input('Choose one of the following: 1.Rock, 2.Paper, 3.Scissors: '))
    computerChoice = random.randint(1, 3)

    # Prints the choice of the computer
    if computerChoice == 1:
        print('\nComputer chooses Rock')
        print(UserChoice(userChoice))
    elif computerChoice == 2:
        print('\nComputer chooses Paper')
        print(UserChoice(userChoice))
    else:
        print('\nComputer chooses Scissor')
        print(UserChoice(userChoice))
    
    # Checks the choice of the computer and the user
    if userChoice == computerChoice:
        print('It\'s a draw\n')
        drawCount += 1
    elif userChoice == 1 and computerChoice == 3:
        print('You win !!!\n')
        winCount += 1
    elif userChoice == 2 and computerChoice == 1:
        print('You win !!!\n')
        winCount += 1
    elif userChoice == 3 and computerChoice == 2:
        print('You win !!!\n')
        winCount += 1
    else:
        print('Computer wins !!!\n')
        loseCount += 1
    
    #Asks user whether he wants to play again
    playAgainConfirmation = input('Do you want to play again Y/N: ')

    if playAgainConfirmation.lower() != 'y':
        game = False

        # Displays the win count and lose count
        print('\n----------------- SESSION SUMMARY ------------------')
        print('Played |', str(winCount + loseCount + drawCount))
        print('Won    |', str(winCount))
        print('Lost   |', str(loseCount))
        print('Draw   |', str(drawCount),'\n')
            



