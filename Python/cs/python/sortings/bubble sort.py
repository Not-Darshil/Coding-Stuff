lst=[100,400,300,600,200]
print("unsorted:",lst)

for i in range (1,len(lst)):
    for w in range(len(lst)-i):
        if lst[w]>lst[w+1]:
            lst[w],lst[w+1]=lst[w+1],lst[w]
print("sorted:",lst)


