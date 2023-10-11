##def ss(lst):
##    c=0
##    c=(lst[0]**2)+(lst[-1]**2)
##    return c
##x=ss([10,12,10,100])
##print(x)
def x(lst):
    c=0
    for w in lst:
        for b in w:
            if b=="a":
                c=c+1
    return c
al=x(["elephant","really"])
print(al)

    
