#String Lists - palindrome

str=input('Provide an input to check if it is a palindrome: ')

if str == str[::-1]:
    print('Your input is a palindrome! ')
else:
    print('Your input is not a palindrome.')



a=[1,2,3,4,5,6,7]
print(a[1:])
print(a[3:])
print(a[:-2])
print(a[6:])
print(a[:])
print(a[5:])
print(a[1:6:2]) #start at index = 1 to index = 6 and at every 2
print(a[1:6:3])
