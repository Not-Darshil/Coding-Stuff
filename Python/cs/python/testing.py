str='compUTER 2020'
print (str)
nw=''
for a in range (len(str)):
 if str[a].isupper():
     nw+=str[a].lower()
 elif str[a].islower():
     nw+=str[a].upper()
 elif str[a].isdigit():
     nw+='$'
 else:
     nw+='*'
print (nw)
