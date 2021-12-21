# Guess game
import random as edgar

print('Hello! What is your name?')
my_name = input()
print(f'{my_name} how lucky do you think you are? How many guesses do you want?')
number_of_guesses = input()
number_of_guesses = int(number_of_guesses)
number_from = input('pick your smallest number for the range, what would you like it to be? ')
number_from = int(number_from)
number_to = input('pick your largest number for the range, what would you like it to be? ')
number_to = int(number_to)
number = edgar.randint(number_from, number_to)
print(f'Well, {my_name} I am thinking of a number between {number_from} and {number_to}.')
    
for guesses_taken in range(number_of_guesses):
    
    if guesses_taken > 0:
        another_word = 'another'
    else: 
        another_word = 'a'
    
    print(f'take {another_word} guess')   
    
    guess = input()
    guess = int(guess)
    
    if guess < number_from or guess > number_to: 
        print('that is out of range, FOOL!')
    elif guess < number: 
        print('that is less than my number')
    elif guess > number:
        print('that is bigger than my number')
    else:
        break 
    
if guess == number:
    guesses_taken = guesses_taken + 1
    print(f'good job, {my_name}! you guessed my number in {guesses_taken} guesses!')

if guess != number:
    print(f'no, the number I was thinking of was {number}')
