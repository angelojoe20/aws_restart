import random

print('Count to 10')
print('')
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")
print('')


for x in range (0,11):
    print(x)

number = random.randint(1,10)
isGuessRight = False

while isGuessRight != True:
    guess = input('Guess the number between 1 to 10: ')
    if int(guess) == number:
        print('You guessed {}. That is correct! You guessed it! '.format(guess))
    else:
        print('You guessed {}. You Failed. Try again.'.format(guess))
    