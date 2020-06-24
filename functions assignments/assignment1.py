#to find max of three numbers 
a=int(input("Enter a first number: "))
b=int(input("Enter a second number: "))
c=int(input("Enter a third number: "))

def max_of_three_numbers(a,b,c):
   max=a if a>b else b
    max=max if max>c else c
    return max
print(max_of_three_numbers(a,b,c))