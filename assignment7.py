def longest_length(*args):
    max_lenth=0
    for k in args:
        if(max_lenth<len(k)):
            max_lenth=len(k)
    return max_lenth


val=longest_length('Golo','salamandar','geographically','and some thing more')
print(val)