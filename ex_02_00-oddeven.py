# PracticePython.org example 2 -
# Determine odd/even number + determine multiple of 4
while True:
    n = input('Enter an integer: ')
    try:
        num_int=int(n)
        if num_int%2==0:
            print(f'{num_int} is an even number.')
            if num_int%4==0:
                print(f'{num_int} is also a multiple of 4')
            break
        else:
            print(f'{num_int} is an odd number.')
            break
    except:
        print('Invalid input. Please enter a number.')
        continue
