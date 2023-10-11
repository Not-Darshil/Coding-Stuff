import pickle
f=open("bina.dat","bw+")
i=23
s="hello"
flt=32.44
l=[45,23,"ram",23.45]
d={"ram":[3,4,5],45:4455}
##in dictionay key must be unique and immutable
##and value may be mutable or immutable or duplicate
pickle.dump(i,f)
pickle.dump(s,f)
f.seek(0)
v=pickle.load(f)
print(v)
v=pickle.load(f)
print(v)
f.close()
