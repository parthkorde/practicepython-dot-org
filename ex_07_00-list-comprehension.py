# List comprehensions - take a list and print only even elements in it
ans=[]
a=[1,4,9,16,25,36,49,64,81,100]
for i in a:
    if float(i)%2==0:
        ans.append(i)
print(a)
print(ans)
