input1=int(input("Enter a number : "))
input2 =int(input("Ranges start from 0  \nGive a max value of  Range :"))
ls=[0]
ls.append(input2)

def check_inrange(val,range1,ls):
    if(val<=range1):
        return f'{val} is within given range {ls}'
    else:
        return f' {val} is out from range {ls}'

print(check_inrange(input1,input2,ls))