input2=int(input("Enter length of List1  : "))
ls=[]
ls1=[]
for i in range(input2):
    ls.append(input("eneter an element "+str(i+1)+":"))
input1=int(input("Enter length of List2  : "))
for i in range(input1):
    ls1.append(input("eneter an element "+str(i+1)+":"))

def add_end(val,val1): 
    res=[]
    for j in range(len(val)):
        if(j==(len(val)-1)):
            for k in val1:
                res.append(k)
        else:
            res.append((val[j])) 
    return res

print(add_end(ls,ls1))