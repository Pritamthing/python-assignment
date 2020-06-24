#to check given dic it empty or not
#ls=[{},{},{}]
ls=[{'1':'3'},{},{}]
val=False
def check_dic(val):
    for j in val:
        if(len(j)>=1):
            val=True
            break

    if(val==True):
        return True
    else:
        return False

print(check_dic(ls))