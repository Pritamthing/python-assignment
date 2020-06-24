val=input("Enter your string Containing uppercase and lower case letters : ")


def count_upper_lower(val):
    pattern='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    count=0
    count1=0
    for j in val:
        if j in pattern:
            print(j)
            count+=1
        elif(j!=' '):
            count1+=1
    
    print('No of Uppercase letters: '+str(count))
    #print('No of Lowercase letters: '+str((len(val)-count)))
    print('No of Lowercase letters: '+str(count1))
count_upper_lower(val)