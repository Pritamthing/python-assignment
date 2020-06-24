input2=int(input("Enter length of List  : "))
ls=[]
cpyls=[]
for i in range(input2):
    ls.append(input("eneter an element "+str(i+1)+":"))
def copy_list(val):
    for j in val:
        cpyls.append(j)
        
    return cpyls

print(copy_list(ls))