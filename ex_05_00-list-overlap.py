# List Overlap
ans=[]
a=[2,2,21,3,4,2,2,2,2]
b=[1,2,3,1,4,2,15,1]

for i in a:
    if i in b:
        if i not in ans:
            ans.append(i)
print(ans)
