num=int(input("Enter a size of dict:"))
dicts={}
for j in range(num):
    dicts[j+1]=int(input("Value at "+str(j+1)+": "))

def sum_dict(val):
    sum=0
    for k in val:
       sum+=val[k]
    return sum

print(sum_dict(dicts))
