input1=input("enter a string: ")
res=''
last=''
end1='ing'
end2='ly'
k=-3
for j in range(3):
    last+=input1[k]
    k+=1
if(len(input1)>=3):
    if(last==end1):
        res=input1+end2
    else:
        res=input1+end1
print(res)