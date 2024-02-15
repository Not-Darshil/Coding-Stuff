f=open("first.txt","w+")
print("write few lines and empty to stop")
while True:
    x=input()
    f.write(x+"\n")
    if x=="":
        break
    
f.seek(0)
lines=f.readlines()
print("file contains",lines)
nol=0
for line in lines:
    cnt=0
    for ch in line:
        if ch.isdigit():
            cnt=cnt+1
            print(ch,cnt)
    print(line,"contains",cnt,"digits")
    if cnt>4:
        nol=nol+1            
print()
print(nol,"lines are containing more than 4 digits")
print()
input()
lst=[]
snol=0
for line in lines:
    words=line.split()
    print("words ",words)    
    scnt=0
    for word in words:        
        if word[-1]=="s":
            scnt=scnt+1
            print("scnt is ",scnt)
    if scnt>3:
        snol=snol+1
        lst.append(line)
print(snol,"(+3)lines have s",sep="")
print()
f.close()
