##fname=input("enter file name")
##count=0             #count of a specific word
##maxcount=0          #maximum among the count of each words
##l=[]                #list to store the words with maximum count
##with open(fname,'r') as f:
##    with open(fname,'r') as f:
##        contents=f.read()
##        words=content.split()
##for i in range(len(words)):
##    for j in range(len(words)):
##        if(words[i]==words[j]):        #finding count of each word
##            count+=1
##        else:
##            count=count
##        if(count==maxcount):          #comparing with maximum count
##            l.append(words[i])
##        elif(count>maxcount):         #if count greater than maxcount
##            l.clear()
##            l.append(words[i])
##            maxcount=count
##        else:
##            l=l
##        count=0
##print(l)






f=open("first.txt","r+")
y=f.read()
k=y.split()
l=[]
ct=0
mct=0
for i in range(len(k)):
    for j in range(len(k)):
        if(k[i]==k[j]):        #finding count of each word
            ct+=1
        else:
            ct=ct
        if(ct==mct):          #comparing with maximum count
            l.append(k[i])
        elif(ct>mct):         #if count greater than maxcount
            l.clear()
            l.append(k[i])
            mct=ct
        else:
            l=l
        ct=0
print(l)

    
