input2=int(input("Enter a length of list you to sum up: "))
ls=[]
for i in range(input2):
    ls.append(int(input()))

def mul(val):
    res=1
    for j in val:
        res*=j
    return res

print(mul(ls))
      
          