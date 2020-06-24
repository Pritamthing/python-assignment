input1=int(input("Enter a number : ")) 

def is_prime(org):
    count=0
    for j in range(org+1):
        if(j!=0):
            if(org%j==0):
                count+=1
    if(count==2):
        return f'{org} is a Prime number.'
    else:
        return f'{org} is not a Prime number.'
print(is_prime(input1))
