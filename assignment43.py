tp1=('p','i','z','z','z','a')
lst=list(tp1)
del lst[4]
print(tuple(lst))
#or 
tp2=tp1[:3]+tp1[4:]
print(tp2)