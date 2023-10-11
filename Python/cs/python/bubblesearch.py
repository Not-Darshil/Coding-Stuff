##k=[23,12,34,56,67,11]
##m=len(k)
##for w in range(len(k)):
##    for b in range(m-1):
##        if k[b]>k[b+1]:
##            k[b],k[b+1]=k[b+1],k[b]
##            
##    m=m-1
##print(k)
##
##
##
##lst=[12,11,10,9,33,89,22]

lst=list(eval(input("Enter no.s")))
m=len(lst)
for w in range(m):
    for a in range(m-1):
        if lst[a]>lst[a+1]:
            lst[a],lst[a+1]=lst[a+1],lst[a]
    m=m-1
print(lst)











            
