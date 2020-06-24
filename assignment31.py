dict1={1:10,2:20,3:30,4:40}
def iterate_dict(d1):
    sum=0
    for k in d1:
        sum+=d1[k]
    return sum

print(iterate_dict(dict1))