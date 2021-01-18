# List all numbers less than 5
print('Please enter an array with n values. Type STOP after n-th value as desired.')
a = []
ans=[]
gate = 1
while True:
    if gate == 1:
        input_value=input('Please enter array element here: ')
    else:
        input_value=input()
    if input_value.lower() == 'stop':
        print(f'Your entered array is: \n\n{a}')
        break
    else:
        try:
            input_value=float(input_value)
            a.append(input_value)
            gate = 0
            continue
        except:
            print('Input is not a number. Please enter a valid number.')
            gate = 1
            continue


while True:
    n=input("To list all numbers in your array below number 'n', enter num. n: ")
    try:
        num_lessthan=float(n)
        for x in a:
            if x<num_lessthan:
                ans.append(x)
        print(f'The list of numbers less than {num_lessthan} in this array are:\n{ans}')
        break
    except:
        print('Invalid input. Please enter a valid number.')
        continue
