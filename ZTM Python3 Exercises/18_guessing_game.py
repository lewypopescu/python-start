from random import randint

import sys

lucky_number = randint(1, 10)

print("Welcome to the Guessing Game!")
print(lucky_number)

while True:
    try:
        guess = int(input("Guess a number between 1 and 10: "))
        if guess < 1 or guess > 10:
            print("Please enter a number between 1 and 10.")
        if guess == lucky_number:
            print("Congratulations! You guessed the lucky number!")
            break
        else:
            print("That's not the lucky number. Try again!")
    except ValueError:
        print("Invalid input. Please enter a valid number between 1 and 10.")

print(f"The lucky number was: {lucky_number}")

print("Now let's play a more advanced game!")

random_number = randint(int(sys.argv[1]), int(sys.argv[2]))
print(f"Now, the random number is between {sys.argv[1]} and {sys.argv[2]}.")
print(f"The random number is: {random_number}")

while True:
    try:
        number = int(
            input('Please choose a number that falls between those two you just chose: '))
        if number >= int(sys.argv[1]) and number <= int(sys.argv[2]):
            if number == random_number:
                print("You're a genius!")
                break
            else:
                print("That's not the lucky number. Try again!")
        else:
            print(
                f"Please enter a number between {sys.argv[1]} and {sys.argv[2]}.")
    except ValueError:
        print("Please enter a number")
        continue

# Good game :)
