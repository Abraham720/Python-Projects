from random import *
print('\nWelcome to \nNumber Guessing game!\n')

again = ''

tries = 0

while again != 'no':
    
    min = int(input("What's the minimum number? "))
    max = int(input("What's the maximum number? "))
    guesses = 1
    rating = ''
    
    number = randint(min, max)
    guess = int(input("\nA random number has been made.\nWhat's your guess? "))
    
     while guess != number:
    
        if guess > number:
            print('\nYou guess too high! Try lower ')
            guess = int(input("\nWhat's your next guess? "))
            guesses += 1

        elif guess < number:
            print('\nYou guess too low! Try higher')
            guess = int(input("\nWhat's your next guess? "))
            guesses += 1
    
    
    if guesses == 1 or guesses == 2:
        rating = 'Imposible!'
    
    elif guesses < 5:
        rating = 'Outstanding!'
    
    elif guesses < 7:
        rating = 'Good'
            
    elif guesses < 9:
        rating = 'Ok'
    
    elif guesses < 11:
        rating = 'Meh'
    
    else:
        rating = 'Bad try'
    
    
    print('\nYou are correct! the number was', number ,'\nYou guess the number within ' , guesses , 'guesses/try!' , rating)
    
    games += 1
        
    again = input('\nDo you want to play again? ')

    if again != 'no' and games <= 3:
        break


if games <= 3:
    print("\n you have win this game 3 times! i'll increase the difficulty now :D")

print("\nThank you for playing! have a nice day :D")
