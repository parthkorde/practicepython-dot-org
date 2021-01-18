# Character input - determine year in which user will be 100 years old
from datetime import date
c_year=date.today().year
while True:
    name=input('Enter your name: ')
    try:
        name_str=int(name)
        print('Invalid input. Name should be alphabetic.')
        continue
    except:
        age=input('Enter your age: ')
    try:
        age_int=int(age)
        age_100=c_year-age_int+100
        o=print(name,', you will be 100 years old in ',age_100)
        break
    except:
        print('Invalid input. Enter age in numbers only. ex: 24')
        continue
while True:
    op_msg=input('Enter the no. of times you want to output this message: ')
    try:
        op=int(op_msg)
        while op>0:
            print(name,', you will be 100 years old in ',age_100)
            op=op-1
        break
    except:
        print('Please enter a valid number.')
        continue
