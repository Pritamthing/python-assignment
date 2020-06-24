       
input2=int(input("Enter length of List  : "))
ls=[]
for i in range(input2):
    ls.append(input("eneter an element "+str(i+1)+":"))
def remove_dublicates(val):
    res=[]
    for j in val:
        if j not in res:
            res.append(j)
    return res

print(remove_dublicates(ls))

      
          