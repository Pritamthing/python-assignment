input2=int(input("Enter length of List  : "))
input1=input("Enter a string to add at the beginning of list items:")
ls=[]
for i in range(input2):
    ls.append(input("eneter an element "+str(i+1)+":"))
def add_begin(val,input1):
    res=[]
    for j in val:
        res.append(input1+j)
    return res

print(add_begin(ls,input1))