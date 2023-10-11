##DARSHIL KUMAR
## XII-A
##


import mysql.connector as con
import datetime
while True:
    try:
        pswd=input("Enter SQL Password:")
        dbobj=con.connect(host="localhost",user="root",password=pswd,charset='utf8')
        print("Connecting....")
        break
    except :
        print("***WRONG PASSWORD***")
        

crsr=dbobj.cursor()
now = datetime.datetime.now()

def dbtable():
    crsr.execute("create database if not exists supermarket")
    crsr.execute("use supermarket")
    crsr.execute("create table if not exists product(PNO int,PNAME char(15),BRAND char(15),MRP int,SELLINGP int,primary key(PNO))")



def intro():
    print()
    print("_"*85)
    print("""
                                DARSHIL SUPEMARKET                   {}
         
    0)EXIT
    1)VIEW PRODUCTS
    2)ADD PRODUCT
    3)REMOVE PRODUCT
    4)GENERATE BILLING
    5)UPDATE PRODUCTS
    """.format(now.strftime('%d-%m-%Y %H:%M')))


    
def intinp(stmnt):
    y=0
    while y==0:
        try:
            x=input(stmnt)
            if bool(int(x))==True:
                y=1
                return int(x)
        except:
            print("****Integer Value Required****")
            
def viewproduct():
    print()
    print("-"*85)
    crsr.execute("desc product;")
    recs=crsr.fetchall()
    print("%3s %-15s %-15s %5s  %5s"%(recs[0][0],recs[1][0],recs[2][0],recs[3][0],recs[4][0]))
    crsr.execute("select * from product;")
    recs=crsr.fetchall()
    for rec in recs:
        print("%3s %-15s %-15s %5s  %5s"%(rec[0],rec[1],rec[2],rec[3],rec[4]))

        


def addproduct():
    print("""
====================================ADD PRODUCT======================================
""")
    try:
        n=intinp("Enter no. of records to be added:")
        for w in range (n):
            try:
                pno=intinp("Enter PNO:")
                pname=input("Enter PNAME:")
                brand=input("Enter BRAND:")
                mrp=intinp("Enter MRP:")
                sellingp=intinp("Enter SELLINGP:")
                record=(str(pno),pname,brand,str(mrp),str(sellingp))
                print(record)
                print()
                confirm=input("Confirm(y/n):")
                print()
                if confirm=="y" or confirm=="Y":
                    crsr.execute("select * from product;")
                    recs=crsr.fetchall()
                    for rec in recs:
                        if rec[0]==record[0]:
                            print("****PNO NOT UNIQUE****")
                            zz=0
                            break
                    if zz==1:
                        if confirm=="y" or confirm=="Y":
                            crsr.execute("insert into product values {}".format(record))
                            crsr.execute("commit")
                            print()
                    else:
                        print('fdf')
            except ValueError:
                print("_____Wrong values_____")     
    except ValueError:
        print("_____Wrong values_____")

def remove(by,val):
    try:
        crsr.execute("select * from product where {}='{}'".format(by,val))
        rec=crsr.fetchall()
        if rec==[]:
            print("EMPTY RECORD")
        else:
            print("Record:")
            print(rec)
            confirm=input("Confirm(y/n):")
            if confirm=="y" or confirm=="Y":
                if by=="pno":                    
                    crsr.execute("delete from product where pno ={}".format(val))
                elif by=="pname":
                    crsr.execute("delete from product where pname = '{}'".format(val))
                elif by=="brand":
                    crsr.execute("delete from product where brand ='{}'".format(val))
                crsr.execute("commit")
                print("RECORD DELETED")
                return
            else:
                pass
    except:
        print("_____Wrong values_____")

##def rem_data_input(stmnt):
##    while y=0:
##        try:
##            data=intinp("")
##        except:
##            pass
    

def removeproduct():
    print("""
===================================REMOVE PRODUCT====================================
""")
    print(""""
    MODES:
    0)EXIT
    1)PNO
    2)PNAME
    3)BRAND    """)
    print("_"*85)
    y=0
    data=""
    while y==0:
        try:
            print()
            mod=input("Enter Mode:")
            if mod=="0":
                y=1
                break
            elif mod=="1" or mod=="pno" or mod=="PNO":
                z=1
                while z==1:
                    try:
                        val=intinp("Enter PNO")
                        if val==0:
                            z=0
                        else:
                            remove("pno",val)
                            z=0
                    except:
                        print("_____Wrong values_____")
            elif mod=="2" or mod=="PNAME" or mod=="pname":
                z=1
                while z==1:
                    try:
                        data=input("Enter PNAME:")
                        if data=="0":
                            z=1
                        else:
                            z=0
                            remove("pname",data)
                    except:
                        print("_____Wrong values_____")  
            elif mod=="3" or mod=="BRAND" or mod=="brand":
                z=1
                while z==1:
                    try:
                        data=input("Enter BRAND:")
                        if data=="0":
                            z=1
                        else:
                            z=0
                            remove("brand",data)
                    except:
                        print("_____Wrong values_____") 
            else:
                print("WRONG MODE SELECTED...")
        except ValueError:
            print("_____Wrong values_____")


def billing():
    print("""
=======================================BILLING=======================================
""")
    viewproduct()
    pnolist=[]
    qtylist=[]
    y=0
    sm=0
    print("ENTER PNO AS 0 TO EXIT")
    print()
    while y==0:
        try:
            no=int(input("Enter PNO:"))
            if no==0:
                sm=0
                disc=0
                tdisc=0
                smprice=0
                print("-"*85)
                crsr.execute("desc product;")
                recs=crsr.fetchall()
                print("%3s  %-15s %-15s %4s  %-3s  %-5s %5s %5s"%(recs[0][0],recs[1][0],recs[2][0],recs[3][0],"QTY","PRICE","DISC","COST"))
                for i in range(len(pnolist)):
                    crsr.execute("select * from product where pno={}".format(pnolist[i]))
                    rec=crsr.fetchone()
                    cost=int(rec[4])*qtylist[i]
                    mrp=int(rec[3])
                    tmrp=mrp*qtylist[i]
                    sm=sm+cost
                    disc=tmrp-cost
                    tdisc=tdisc+disc
                    smprice=smprice+tmrp
                    print("%3s  %-15s %-15s %4s  %3s  %5s %5s %5s"%(rec[0],rec[1],rec[2],rec[3],qtylist[i],rec[3]*qtylist[i],disc,cost))
                print("%58s %6s"%("TOTAL PRICE:",smprice))
                print("%58s %6s"%("TOTAL DISCOUNT:",tdisc))
                print("%58s %6s"%("AMOUNT TO BE PAID:",sm))
                y=1
                break
            else:
                z=0
                while z==0:    
                    crsr.execute("select * from product where pno={}".format(no))
                    rec=crsr.fetchone()
                    if rec==None:
                        print("No such product available")
                        z=1
                        break
                    qty=int(input("Enter Qty:"))
                    cost=int(rec[4])*qty
                    sm=sm+cost
                    crsr.execute("desc product;")
                    recs=crsr.fetchall()
                    print("%3s %-15s %-15s %5s  %8s %5s %4s"%(recs[0][0],recs[1][0],recs[2][0],recs[3][0],recs[4][0],"QTY","COST"))
                    print("%3s %-15s %-15s %5s  %8s %5s %4s"%(rec[0],rec[1],rec[2],rec[3],rec[4],qty,cost))
                    print()
                    pnolist.append(no)
                    qtylist.append(qty)
                    break
        except ValueError:
            print("_____Wrong values_____")



def update(mod,val):
    try:
        crsr.execute("select * from product where {}='{}'".format(mod,val))
        rec=crsr.fetchall()
        if rec==None:
            print("EMPTY RECORD")
        else:
            print("Record:")
            print(rec)
            confirm=input("Confirm(y/n):")
            if confirm=="y" or confirm=="Y":
                if mod=="pno":
                    newrec=intinp("Enter NEW PNO:")
                    crsr.execute("update product set pno={} where pno={}".format(newrec,val))
                elif mod=="pname":
                    newrec=input("Enter NEW PNAME:")
                    k="update product set pname= '"+ newrec+"' where pname= '"+val + "'"
                    crsr.execute(k)
                elif mod=="brand":
                    newrec=input("Enter NEW BRAND:")
                    k="update product set brand= '"+ newrec+"' where brand= '"+val + "'"
                    crsr.execute(k)
                elif mod=="mrp":
                    newrec=intinp("Enter NEW MRP:")
                    crsr.execute("update product set mrp={} where mrp={}".format(newrec,val))
                elif mod=="sellingp":
                    newrec=intinp("Enter NEW SELLINGP:")
                    crsr.execute("update product set sellingp={} where sellingp={}".format(newrec,val))
                crsr.execute("commit")
                print("RECORD UPDATED")
                return
            else:
                pass
    except:
        print("_____Wrong values_____")


def updateproduct():
    print("""
===================================UPDATE PRODUCT====================================
""")
    print("""
    0)EXIT
    1)PNO
    2)PNAME
    3)BRAND
    4)MRP
    5)SELLINGP
    """)
    y=0
    data=""
    while y==0:
        try:
            print()
            mod=input("Enter Mode:")
            if mod=="0":
                y=1
                break
            elif mod=="1" or mod=="pno" or mod=="PNO":
                z=1
                while z==1:
                    try:
                        val=intinp("Enter CURRENT PNO: ")
                        if val==0:
                            z=0
                        else:
                            update("pno",val)
                            z=0
                    except:
                        print("_____Wrong values_____")
            elif mod=="2" or mod=="PNAME" or mod=="pname":
                z=1
                while z==1:
                    try:
                        data=input("Enter PNAME:")
                        if data=="0":
                            z=1
                        else:
                            z=0
                            update("pname",data)
                    except:
                        print("_____Wrong values_____")  
            elif mod=="3" or mod=="BRAND" or mod=="brand":
                z=1
                while z==1:
                    try:
                        data=input("Enter BRAND:")
                        if data=="0":
                            z=1
                        else:
                            z=0
                            update("brand",data)
                    except:
                        print("_____Wrong values_____")
            elif mod=="4" or mod=="MRP" or mod=="mrp":
                z=1
                while z==1:
                    try:
                        data=intinp("Enter CURRENT MRP:")
                        if data=="0":
                            z=1
                        else:
                            z=0
                            update("mrp",data)
                    except:
                        print("_____Wrong values_____")
            elif mod=="5" or mod=="SELLINGP" or mod=="sellingp":
                z=1
                while z==1:
                    try:
                        data=intinp("Enter CURRENT SELLINGP:")
                        if data=="0":
                            z=1
                        else:
                            z=0
                            update("sellingp",data)
                    except:
                        print("_____Wrong values_____")
            else:
                print("WRONG MODE SELECTED...")
        except ValueError:
            print("_____Wrong values_____")
    

            
def main():
    dbtable()
    while True:
        input()
        intro()
        option=input("Enter Option")
        if option=="1":
            viewproduct()
        elif option=="2":
            addproduct()        
        elif option=="3":
            removeproduct()
        elif option=="4":
            billing()
        elif option=="5":
            updateproduct()
        elif option=="0":
            print("Thanks for visiting...")
            break
        else:
            print("Try Again")
main()
        
    
    
