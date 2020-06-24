input1=input("Enter a String: ")

def unique_sorted(input1):
    res=[]
    unique=input1.split(',')
    for i in  unique:
        if(i not in res):
            res.append(i)
    return res
        
          

val=unique_sorted(input1)
print(sorted(val))