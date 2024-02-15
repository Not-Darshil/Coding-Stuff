def fx(k,w):
    u=len(k)-1
    l=0
    while l<=u:
        m=(u+l)//2
        if w==k[m]:
            return(m)
        elif w<k[m]:
            u=m-1
        else:
            l=m+1
    return(-1)             
lst=[12,14,17,19,22,24,26,28]
print(lst)
x=int(input("ENTER NO. TO BE SEARCHED"))
y=fx(lst,x)
if y==-1:
    print("ELEMENT NOT FOUND")
else:
    print(x,"FOUND AT",y)
