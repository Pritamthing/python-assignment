input1=input("Enter a String: ")

def exchange_char(input1):
    first=input1[0]
    last=input1[-1]
    res=''
    for i in range(len(input1)-1):
        if i==0 :
              res+=last
        else:
            res+=input1[i]
    res+=first
    return res
        
          

val=exchange_char(input1)
print(val)