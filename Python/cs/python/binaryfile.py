import pickle
f=open("emp.txt","bw+")
print("ENTER DATA AND 0 ENO TO EXIT ")
while True:
    lst=[]
    eno=int(input("Enter Eno."))
    name=input("Enter Name")
    salary=int(input("Enter Salary"))
    if eno==0 or salary=0:
        break
    else:
        lst.append(eno)
        lst.append(name)
        lst.append(salary)
    pickle.dump(lst,f)
f.seek(0)
sl=0
try:
    while True:
        y=pickle.load(f)
        print("Eno",y[0])
        print("Name",y[1])
        print("Salary",y[2])
        sl=sl+int(y[2])
        print()
except EOFError:
    print("No More Records")


print("Total Salary",sl)    
print("ABOVE 50000 SALARY")
try:
    while True:
        y=pickle.load(f)
        if int(y[2])>50000:
            print(y[1])
except EOFError:
    print("No More Records above 50000")



    
