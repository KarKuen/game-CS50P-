import random

def main():
    while True:
        level = input('Level: ')
        try:
            if int(level) >= 0:
                integer = random.randint(1, int(level))
                randomnumber(integer)
        except ValueError:
            pass

def randomnumber(integer):
    while True:
        guess = int(input('Guess: '))
        if guess >= 0:
            if guess < integer:
                print('Too small!')
            elif guess > integer:
                print('Too large!')
            else:
                print('Just right!')
                sys.exit()

main()