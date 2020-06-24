
a1=[1,2,3,4,5,6]
a2=[4,5,6,7,8,9]

val=list(filter(lambda x: x in a1,a2))
print(val)