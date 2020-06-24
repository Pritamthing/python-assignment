num=int(input("Enter a size of dict:"))
dicts={}
for j in range(num):
    dicts[j+1]=input("Value at "+str(j+1)+": ")

def iterate_dict(val):
    for k in val:
        print("Val at "+str(k)+" iteartion is:"+val[k])

iterate_dict(dicts)