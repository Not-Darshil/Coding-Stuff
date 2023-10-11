lst=[10,20,30,40,50]
print(lst)
el=int(input("enter no."))
l=0
up=len(lst)-1
while up>=l:
    m=(up+l)//2
    if lst[m]==el:
        print("element found at",m)
        break
    elif lst[m]<el:
        l=m+1
    else:
        up=m-1
else:
    print("element not found")
