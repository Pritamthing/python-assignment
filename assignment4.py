input1=input("enter first string: ")
input2=input("enter Second  string: ")
#varibles req 
res=''
res1=''
ta=''
tb=''
for i in range(2):
    ta+=input1[i]
    tb+=input2[i]
    i+=1
count=0
# to ensure for all unequal length of two string 
for j in input1:
    if(count>=2):
        res+=j
    count+=1
count=0
for j in input2:
    if(count>=2):
        res1+=j
    count+=1

res=tb+res
res1=ta+res1
print(res+' '+res1)