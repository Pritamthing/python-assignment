tp=[(2,5),(1,2),(2,3),(4,4),(2,1)]
ls=[]
ta=(1,3)
ta=reversed(ta)
def sort_tuple(tp):
    for i in tp:
        i=reversed(i)
        ls.append(tuple(i))
    return sorted(ls)

val=sort_tuple(tp)
ls1=[]
for j in val:
    j=reversed(j)
    ls1.append(tuple(j))
print(ls1)

      
          