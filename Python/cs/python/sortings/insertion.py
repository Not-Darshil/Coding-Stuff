lst=[10,40,30,50,11,79]
for w in range (1,len(lst)):
    pick=lst[w]
    up=w-1
    while up>=0 and pick<lst[up]:
        lst[up+1]=lst[up]
        up=up-1
    else:
        lst[up+1]=pick
print(lst)











'''


l=[15,11,30,20,25]
print("unsorted",l)
for w in range(1,len(l)):
    print()
    print("step",w)
    print(l)
    pick=l[w]
    up=w-1
    while up>=0 and pick<l[up]:
        l[up+1]=l[up]
        up=up-1
    else:
        l[up+1]=pick
print(l)
'''
