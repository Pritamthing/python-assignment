input1=input("Enter a String: ")

def remove_odd_index(input1):
    res=[]
    unique=input1.split(' ')
    for i in  unique:
        if(i not in res):
            res.append(i)
    dicts={}
    for j in res:
        count=0
        for k in unique:
            if j==k:
                count+=1
        dicts[j]=count
    return dicts
        
          

val=remove_odd_index(input1)
print(val)