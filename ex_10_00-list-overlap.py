# List overlap comprehensions

a = [1,1,2,3,5,8,13,21,34,55,89]
b = [1,2,3,4,5,6,7,8,9,10,11,12,13]
ans=[]
for count in a:
    print(count)
    if count in b:
    #     print('this works')
    # else:
    #     print('something is wrong')
        if count not in ans:
            ans.append(count)
            print(ans)
print(a)
print(b)
print(ans)



# NOTE: if count in b > returns TRUE
# if count in b==True is a WRONG SYNTATIC STATEMENT! ! ! 
