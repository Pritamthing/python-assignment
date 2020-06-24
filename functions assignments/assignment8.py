input1=int(input("Enter a size of list : ")) #seting  the size of list by user
ls=[] #declaration of list ls with null/none values
for i in range(input1):
    ls.append(input("Enter element at "+ str(i+1) +" : "))

def unique_lst(org):
    unique=[]
    for i in org:
        if i not in unique:
            unique.append(i)
    return unique
print(unique_lst(ls))
