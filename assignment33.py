input1=15
def gen_dict(num):
    res={}
    for k in range(num+1):
        if(k>=1):
            res[k]=k*k
    return res

print(gen_dict(input1))