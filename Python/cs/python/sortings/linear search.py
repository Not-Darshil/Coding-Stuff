lst=[10,50,30,70,20]
n=int(input("Enter No to be searched"))
for w in range (len(lst)):
    if lst[w]==n:
        print("Element Found at",w)
        break
else:
    print("element not found")




