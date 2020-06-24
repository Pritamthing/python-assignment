dict1={1:10,2:20}
key=int(input("enter a key:"))
def check_dictkey(d1,key):

    if key in d1:
        print("Key Already exists")
    else:
        data=int(input("add data:"))
        d1[key]=data


    
    return d1

print(check_dictkey(dict1,key))