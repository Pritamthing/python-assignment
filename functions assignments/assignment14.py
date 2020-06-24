dicts={'a':'apple','c':'cat','b':'ball'}
val=lambda x:sorted(x)#sorting keys and then values
ok=val(dicts)
sortdict={}
for j in ok:
    sortdict[j]=dicts[j]
print(sortdict)
