import random
computer_guess_number = random.randint(1, 10)

player_name = input("Hi My name is shaishav, What is your name?")
number_of_guesses = 0
print('Greatings '+ player_name+ ' Lets  play Random guessing game')
print("My guess is between 1 to 100")

while number_of_guesses < 6:
    user_guess = int(input())
    number_of_guesses += 1
    if user_guess < computer_guess_number:
        print('Please Guess higher number')
    if user_guess > computer_guess_number:
        print('Please guess lower number')
    if user_guess == computer_guess_number:
        break
if user_guess == computer_guess_number:
    print('You have guessed the right number in ' + str(number_of_guesses) + ' tries')
else:
    print('You tired 6 times, however the right  number was ' + str(computer_guess_number))