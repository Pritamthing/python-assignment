from functools import reduce
fibo=lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2),[0,1])
print(fibo(8))