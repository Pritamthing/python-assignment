input2=input("Enter a html tag-name to generate: ")
input1=input("Enter a String: ")


def html_tags(input1,input2):
    html='<'+input2+'>'+ input1+'</'+input2+'>'
    #html= ['<'+input2+'>' +input1+' </'+input2'>']
    return html
        
          

val=html_tags(input1,input2)
print(val)