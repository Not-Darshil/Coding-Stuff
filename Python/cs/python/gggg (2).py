'''
f=open("first.txt","r+")
c=0
while True:
        x=f.readline()
        if len(x)==0:
                break
        if "student" in x:
                print(x)
        if x[-2]=="s":
                c=c+1
        
print("count of s is ",c)
        
'''
f=open('first.txt',"r")
x=f.readlines()
for w in x:
        print(w)
