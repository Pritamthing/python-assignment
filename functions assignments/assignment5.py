#to sum all the members in a list
num=int(input("Enter a number : "))
if(num<0):
    print("sorry!, factorial for negative number does not exists.")
    exit()

def factorial(val):
    #fact using recursion

    if(val==0):
        return 1
    else:
        return val*factorial(val-1)

print(factorial(num))