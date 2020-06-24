input1=input("Enter a String : ")
res=''
res1=[]
if len(input1)<2:
    print("Empty String")
else:
    count=0
    k=-1
    input1=list(input1)
    for j in input1:
        if(count==2):
            break
        res+=j
        res1+=input1[k]
        k-=1
        count+=1
l=-1
for j in res1:
    res+=res1[l]
    l-=1
print(res)