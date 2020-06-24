#to read any input from users
val=input("Enter a String : ")
# str1 for temporary to make unique str
str1=''
#declaration of null dict dicts
dicts={}
#main logic
for i in  val:
    if(i not in str1):
        str1+=i
        print(str1)
    for j in str1:
        count=0
        for k in val:
            if(j==k):
                count+=1
            dicts[j]=count
# need to use sort for making max count as ahead of all 
print(dicts)
    
