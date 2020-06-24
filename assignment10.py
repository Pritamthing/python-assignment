input1=input("Enter a String: ")

def remove_odd_index(input1):
    res=''
    for i in input1[::2]:
        res+=i

    return res
        
          

val=remove_odd_index(input1)
print(val)