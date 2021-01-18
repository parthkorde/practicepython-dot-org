# List all numbers less than 5
print('Please enter an array with n values. Type STOP after n-th value as desired.')
a = []
ans=[]
while True:
    input_value=input('Please enter array element here: ')
    if input_value.lower() == 'stop':
        print(f'Your entered array is: \n\n{a}')
        print(f'The list of numbers less than 5 in this array are:\n{ans}')
        break
    else:
        try:
            input_value=float(input_value)
            if input_value<5:
                ans.append(input_value)
            a.append(input_value)
            continue
        except:
            print('Input is not a number. Please enter a valid number.')
            continue
