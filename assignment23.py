input2=int(input("Enter length of List  : "))
ls=[]
for i in range(input2):
    ls.append(input("eneter an element "+str(i+1)+":"))
def check_list(val):
    if(len(val)<1):
        return 'Empty List'
    else:
        return " Non Empty List"

print(check_list(ls))