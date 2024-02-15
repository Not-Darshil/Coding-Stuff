def fx():
    f=open("india.txt","w+")
    while True:
        x=input("Enter Lines")
        if x=="":
            break
        f.write(x+"\n")
    f.close()
def fy():
    f1=open("india.txt","r")
    f2=open("capital.txt","w+")
    rdlist=f1.read()
    lst=rdlist.split("\n")
    print(lst)
    for w in lst:
        if len(w)!=0:
            if w[0].isupper():
                f2.write(w+"\n")
    print("INDIA.TXT")
    f1.seek(0)
    lst=f1.read()
    k=lst.split()
    print(k)
    print("CAPITAL.TXT")
    f2.seek(0)
    lst=f2.read()
    k=lst.split()
    print(k)
        
            
    
fx()
fy()
            
