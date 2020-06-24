input1=int(input("Enter a size of dict1: "))
dict1={}
for i in range(input1):
    key=input("Enter a key: ")
    dict1[key]=input("Enter a value at "+str(i+1)+": ")
input2=int(input("Enter size of dict2: "))
dict2={}
for j in range(input2):
    key=input('Enter a key: ')
    dict2[key]=input("Enter a value at "+str(j+1)+": ")
def merge_dict(dict1,dict2):
    for k in dict2:
        dict1[k]=dict2[k]
    return dict1

print(merge_dict(dict1,dict2))