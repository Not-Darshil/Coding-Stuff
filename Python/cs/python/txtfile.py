f=open("first.txt","r+")
lstw=[]
lstf=[]
fi=f.read()
file=fi.split()
print(file)
for word in file:
    if word not in lstw:
        lstw.append(word)
        lstf.append(int(1))
    else:
        ind=lstw.index(word)
        lstf[ind]=lstf[ind]+1
             
grt=lstf[0]
print(lstw)
print(lstf)
for ind in range(len(lstf)):
    if grt<lstf[ind]:
        grt=lstf[ind]
for x in range(len(lstf)):
    if lstf[x]==grt:
       print("GRT:",lstw[x],lstf[x]) 
    











