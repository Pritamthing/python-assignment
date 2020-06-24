input1=input("Enter a String : ")
res=''
res+=input1[0]
val=res
i=1
for j in input1:
    #for handling index out of range problem
    if(i<len(input1)):
        if(val==input1[i]):
            res+='$'
        else:
            res+=input1[i]
        i+=1
print(res)

