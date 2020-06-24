       
input2=int(input("Enter a length of list : "))
ls=[]
for i in range(input2):
    ls.append(int(input()))

def largest(val):
    res=val[0]
    for j in val:
        if(j>res):
            res=j
    return res

print(largest(ls))

      
          