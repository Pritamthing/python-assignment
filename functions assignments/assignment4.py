#to sum all the members in a list
val=input("Enter a String : ")
def reverse_str(val):
    res=''
    #without using builtin function reversed
    k=-1
    for j in val:
        res+=val[k]
        k-=1
    return res
print(reverse_str(val))