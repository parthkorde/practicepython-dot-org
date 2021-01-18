# Find out divisors of a number.
print('\n\nThis program lists out all the divisors of a number entered.')
print("If you don't know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26/13 has no remainder.\n")

while True:
    print('Please enter STOP to terminate the program.')
    while True:
        ans=[]
        num=input('\nEnter an integer: ')
        try:
            if num.lower()=='stop':
                break
            else:
                n=int(num)
                for i in range(1,n):
                    if n%i==0:
                        ans.append(i)
                ans.append(n)
                print(ans)
            continue
        except:
            print('Invalid input. Please enter an INTEGER.')
            continue
    break
