input1=input("Enter a String: ")
index=int(input("Enter a index for removing char at: "))

def remove_char(index,input1):
    res=''
    for i in range(len(input1)):
        if i!=index :
              res+=input1[i]
    
    return res
        
          

val=remove_char(index,input1)
print(val)