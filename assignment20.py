       
input2=int(input("Enter a length of list : "))
ls=[]
for i in range(input2):
    ls.append(input())

def count_word_palindrome(val):
    count=0
    for i in val:
        if(len(i)>=2):
            first=i[0]
            last=i[-1]
            if(first==last):
                count+=1
    return count

print(count_word_palindrome(ls))

      
          