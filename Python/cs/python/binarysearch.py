def bs(ls,ele):
    l=0
    u=len(ls)-1
    while l<=u:
        m=(l+u)//2
        if ele==ls[m]:
            return m
        elif ele<ls[m]:
            u=m-1
        else:
            l=m+1
    return -1

l=[1,3,4,8,9,12,16,20]
print (l)
w=input('enter element to be searched ')
result=bs(l,w) #9 #4
if result==-1:
    print ('element not found')
else:
    print ('element found at index',result)
