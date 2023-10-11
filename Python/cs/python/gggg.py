##f=open("fst.txt","w+")
##while True:
##	if len(f.readline())==0:
##		break
##	else:
##		print(f.readline())
##f.close()
print("enter few lines ")
f=open("first.txt","w+")
while True:
    s=input()
    f.write(s+"\n")
    if s=="":
        break
f.seek(0)
print("content of file")
while True:
    
    content=f.readline()
    print(content,end='')
    if len(content)==0:
        break
f.close()
