##'''
##A binary file data.dat is containing
##multiple of objects. You have to count
##that how many of them are strings,
##integers, floats, tuples and others.
##'''
##
##
##import pickle
##f=open("data.dat","bw+")
##s=0
##i=0
##flt=0
##t=0
##ot=0
##pickle.dump("hello",f)
##pickle.dump("hi",f)
##pickle.dump(("hello","hi"),f)
##pickle.dump(9871,f)
##pickle.dump(987.02,f)
##pickle.dump([64,11],f)
##pickle.dump("hello",f)
##f.seek(0)
##print("File contains:")
##try:
##    while True:
##        item=pickle.load(f)
##        print(item)
##        if type(item)==type("string"):
##            s=s+1
##        elif type(item)==type(983):
##            i=i+1
##        elif type(item)==type(89.56):
##            flt=flt+1
##        elif type(item)==type(("tuple",56)):
##            t=t+1
##        else:
##            ot=ot+1
##except EOFError:
##    print()
##    print("String Count",s)
##    print("Integer Count",i)
##    print("Float Count",flt)
##    print("Tuple Count",t)
##    print("Others Count",ot)
##            
import pickle
f=open("int.dat","bw+")
lst=[]
ilst=[56,12,69,87,1,2,11,33,1,14,19,24]
for w in ilst:
    pickle.dump(w,f)
f.seek(0)
try:
    while True:
        item=pickle.load(f)
        if item>33:
            lst.append(item)
except EOFError:
    print("List created",lst)
f.close()


f=open("int.dat","bw")
for w in lst:
    pickle.dump(w,f)
f.close()

print("UPDATED FILE CONTENT")
f=open("int.dat","br")
try:
    while True:
        item=pickle.load(f)
        print(item)
except EOFError:
    print("No More Data")




