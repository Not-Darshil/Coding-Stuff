main={}
for w in range (2):
    name=input("enter name")
    mn=input("enter mobile no.")
    adr=input("enter address")
    mail=input("enter mail")
    k={}
    k["name"]=name
    k["address"]=adr
    k["mail"]=mail
    main[mn]=k
print(main)
print(tuple(main.items()))


    
    

