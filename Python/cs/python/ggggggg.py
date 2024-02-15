print("enter few lines ")
f=open("stu.txt","w+")
while True:
    s=input()
    f.write(s+"\n")
    if s=="":
        break
f.seek(0)

r=f.readlines()
print("content ",r)
l=0
for a in r:
    print(a)
    c=0
  
##    for i in range(len(a)):
##        
##        if a[i].isdigit():
##            c+=1
##    print("no of digit in " ,a,"is",c)
##    if c>4:
##        l+=1
##    p=a.split()   
##    word=0
##    line=0
##    li=[]
##    for x in p:
##        if x[-1]=="s":
##            word+=1
##    if word>3:
##        line+=1
##        li.append(a)
##print("no of sentences in which more than 4 digit present ",l)
##print("no of sentence having more than 3 words ending with s in a line ",line)
##print("lines ",li)
##            
##            
##        
##f.close()
