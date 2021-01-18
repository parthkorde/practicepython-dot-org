# Guess the number - high low exact !
import random
count=1
num_com = random.randint(0,9)
while True:
    # print(num_com)  #line to test if a new random number is generated after every correct guess
    n = input('\n\n\nPlease enter an integer between 0 to 9: ')
    if n.lower()=='stop':
        break
    try:
        num=int(n)
        if num<num_com:
            print('\nYour guess is too less !')
            count=count+1
            continue
        elif num>num_com:
            print('\nYou guess is too high !')
            count=count+1
            continue
        else:
            print('\n------You guessed the right number !-------')
            print(f'\nYou took {count} guesses to get the answer right !')
            count=0
            num_com = random.randint(0,9)
            continue
    except:
        print('\nInvalid input. Please try again with an interger')
        continue
    break
