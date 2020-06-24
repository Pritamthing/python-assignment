num=int(input("Enter a size of dict:"))
dicts={}
for j in range(num):
    dicts[j+1]=int(input("Value at "+str(j+1)+": "))

def mul_dict(val):
    mul=1
    for k in val:
       mul*=val[k]
    return mul

print(mul_dict(dicts))

