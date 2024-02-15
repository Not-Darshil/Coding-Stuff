f=open("file.txt","w+")
print("write lines and empty for exit")
lst=[]
while True:
    x=input()
    if x=="":
        break
    else:
        lst.append(x+"\n")
f.writelines(lst)
f.seek(0)
k=f.readlines()
print(k)
