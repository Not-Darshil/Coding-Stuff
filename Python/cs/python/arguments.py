##def fx(p=10000,r=7):
##    interest=(p*r)/100
##    amt=p+interest
##    print(amt)
##fx()
##
##
import pickle
f=open("bfile.dat","bw+")
k=["hello","hi",123,45,987,"ok","gg13"]
for w in k:
    pickle.dump(w,f)
f.seek(0)
while True:
    try:
        rd=pickle.load(f)
        print(rd)
    except EOFError:
        break
f.close()


def fx(bfile="bfile.dat"):
    f=open(bfile,"br+")
    import pickle
    sm=0
    while True:
        try:
            rd=pickle.load(f)
            if type(rd)==int or type(rd)==float:
                sm=sm+rd
        except EOFError:
            break
    print("SUM:",sm)
fx() 
            
    
    
