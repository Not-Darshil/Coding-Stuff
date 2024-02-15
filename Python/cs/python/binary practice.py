import pickle
f=open("bfile.dat","bw+")
k=["uday","mohit","rohan","uday","ashutosh"]
for w in k:
    pickle.dump(w,f)
print("Old content")
f.seek(0)
try:
    while True:
        item=pickle.load(f)
        print("item",item)
except EOFError:
    print("No More Data")
f.close()

def replace (x,y):
    lst=[]
    f=open("bfile.dat","br+")
    try:
        while True:
            item=pickle.load(f)
            print("items:",item)
            if item==x:
                lst.append(y)
            else:
                lst.append(item)
    
    except EOFError:
        print("file ended")
        print(lst)
    f.close()
    f=open("bfile.dat","bw")
    for w in lst:
        pickle.dump(w,f)
    
    f.close()
    f=open("bfile.dat","br+")
    print("Updated File Content:")
    try:
        while True:
            item=pickle.load(f)
            print(item)
    except EOFError:
        print("No More Data")
replace("uday","shubham")                
                
                
                
    
