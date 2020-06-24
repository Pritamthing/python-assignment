in1=input('Enter a String: ')

val=lambda x: 'Integer' if(x.isdigit()) else 'String'
print(val(in1))
