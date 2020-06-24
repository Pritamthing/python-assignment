num=int(input("Enter a size of dict:"))
dicts={}
for j in range(num):
    dicts[j+1]=int(input("Value at "+str(j+1)+": "))
key=int(input("Enter a key to remove"))

def removekey_dict(val,key):
    # del val[key]
    val.pop(key)
    return val

print(removekey_dict(dicts,key))
 
