import random


def do_stuff(number=0):
    try:
        if number:
            number = int(number)
            print(f"Doing stuff with {number}...")
            return number * 3
        else:
            return "plese provide a number"
    except ValueError as err:
        return err


def run_guess(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print('you are a genius!')
            return True
    else:
        print('hey yoo, I said 1-10')
        return False


if __name__ == '__main__':
    answer = random.randint(1, 10)
    while True:
        try:
            guess = int(input('guess a number 1-10:  '))
            if (run_guess(guess, answer)):
                break
        except ValueError:
            print('please enter a number')
            continue
