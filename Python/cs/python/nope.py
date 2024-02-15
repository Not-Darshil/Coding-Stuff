m=(1,2,3,4,4,6,7,8,8)
k=list(m)
for  w in k:
    print("It is",w,"DO YOU WANNA CHANGE")
    y=input()
    if y=="change":
        t=input("enter new value")
        k[k.index(w)]=t
        print("list updated")
print(list(m),"changed to",k)
