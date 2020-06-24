input1=int(input("Enter a size of list : ")) #seting  the size of list by user
ls=[] #declaration of list ls with null/none values
for i in range(input1):
    ls.append(int(input("Enter element at "+ str(i+1) +" : ")))

def even_number(org):
    even=[]
    for i in org:
        if(i%2==0):
            even.append(i)
    return even
print(even_number(ls))
