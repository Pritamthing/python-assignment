#to sum all the members in a list
num=int(input("Enter size of list: "))
lst=[]
for i in range(num):
    item=int(input("Enter an element at "+str(i+1)+": "))
    lst.append(item)

def sum_of_list(val):
    res=0
    #without using builtin function sum
    for j in val:
        res+=j
    return res
print(sum_of_list(lst))