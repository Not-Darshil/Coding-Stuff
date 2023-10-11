p=""
b=input("enter string")
for w in range(-1,-len(b)-1,-1):
    p=p+b[w]
if b==p:
    print("it is ")
else:
    print("NOPE")

