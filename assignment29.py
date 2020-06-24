dict1={1:10,2:20}
dict2={3:30,4:40}
dict3={5:50,6:60}
res={}
def check_dictkey(d1,d2,d3):
    res={}
    for k in dict1:
        res[k]=d1[k]
    for k in dict2:
        res[k]=d2[k]
    for k in dict3:
        res[k]=d3[k]

    
    return res

print(check_dictkey(dict1,dict2,dict3))