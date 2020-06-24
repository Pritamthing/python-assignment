input1=input("enter a string: ")
sub1='not'
sub2='poor'
res=''
val=False
val1=False
str1=input1.split(' ')
for i in str1:
    if(i==sub1):
        break
    else:
        res+=i+' '
for j in str1:
    if j==sub1:
        val=True
    if j==sub2:
        val1=True
if(val and val1):
    res+='good'
else:
    res+=''
print(res)