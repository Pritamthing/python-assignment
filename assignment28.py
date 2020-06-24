dics={2:10,3:20}
def gen_a_key(dicts):
    j=0
    val=0
    for j in dicts:
        val+=dicts[j]
    dicts[j+1]=val
    return dicts


print(gen_a_key(dics))