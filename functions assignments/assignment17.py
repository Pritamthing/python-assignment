str1="saman"
c1='s'

def check_chars(s,c):
    #pints all list  if yes else list as no
    val=lambda x: 'True' if(c in s[0]) else 'False'
    print(val(c))
check_chars(str1,c1)