item=["Eraser",100,"5"]
item2=["Pencil",200,"5"]
item3=["Sharpener",100,"5"]
user=int(input("ENTER USERNAME : "))
pasw=int(input("ENTER PASSWORD : "))
for b in range(1,26,1):
    USER=1000+b
    PASS=2000+b
    if user==USER:
        if PASS==pasw:
            print("Type 1 for updating")
            print("Type 2 for checking")
            print("Type 3 for exit")
            z=int(input("Type your choosen option "))
            if z==1:
                print("The lists are :")
                print("item",item)
                print()
                print("item2",item2)
                print()
                print("item3",item3)
                print()
                x=input("Enter product code ")
                print()
                print()
                print("For updating Qty press 1")
                print("For updating MRP press 2")
                print("For updating Product name press 3")
                print()
                print()
                print()
                if x=="item":
                    g=item
                    t=int(input("Type your choosen option "))
                    if t==1:
                        f=int(input("enter the updated qty"))
                        g[1]=f
                    elif t==2:
                        f=int(input("enter the updated MRP"))
                        g[2]=f
                    elif t==3:
                        f=input("enter the updated product name")
                        g[0]=f
                    else:
                        print("WRONG PRODUCT CODE")
                    print("UPDATED ITEM LIST IS",item)
                
                elif x=="item2":
                    g=item2
                    t=int(input("Type your choosen option "))
                    if t==1:
                        f=int(input("enter the updated qty"))
                        g[1]=f
                    elif t==2:
                        f=int(input("enter the updated MRP"))
                        g[2]=f
                    elif t==3:
                        f=input("enter the updated product name")
                        g[0]=f
                    else:
                        print("WRONG PRODUCT CODE")
                    print("UPDATED ITEM LIST IS",item2)
                elif x=="item3":
                    g=item3
                    t=int(input("Type your choosen option "))
                    if t==1:
                        f=int(input("enter the updated qty"))
                        g[1]=f
                    elif t==2:
                        f=int(input("enter the updated MRP"))
                        g[2]=f
                    elif t==3:
                        f=input("enter the updated product name")
                        g[0]=f
                    else:
                        print("WRONG PRODUCT CODE")
                    print("UPDATED ITEM LIST IS",item3)
                
            elif z==2:
                print(item,item2,item3)
            else:
                print('BYE HAVE A GOOD DAY')

        else:
            print("YOUR PASSWORD IS INCORRECT")



