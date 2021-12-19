#Guess game
import random as r

print('Hello! What is your name?')
my_name = input()

number = r.randint(1,20)
print(f'Well, {my_name} I am thinking of a number between 1 and 20.')
    
for guesses_taken in range(6):
    print('take a guess')
    guess = input()
    guess = int(guess)
    
    if guess < number: 
        print('that is less than my number')
    elif guess > number:
        print('that is bigger than my numer')
    else:
        break 
    
if guess == number:
    guesses_taken = guesses_taken + 1
    print(f'good job, {my_name}!' you guessed my number in {guesses_taken} guesses!
    print ('good job, you win') 
