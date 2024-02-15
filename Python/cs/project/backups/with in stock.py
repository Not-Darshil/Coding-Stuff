import mysql.connector as con
import datetime
import time
while True:
    try:
        pswd=input("Enter SQL Password:")
        dbobj=con.connect(host="localhost",user="root",password=pswd,charset='utf8')
        print("Connecting....")
        time.sleep(2)
        break
    except :
        print("***WRONG PASSWORD***")
        

crsr=dbobj.cursor()
now = datetime.datetime.now()

def dbtable():
    crsr.execute("create database if not exists supermarket")
    crsr.execute("use supermarket")
    crsr.execute("create table if not exists product(PNO int,PNAME char(20),BRAND char(20),MRP int,SELLINGP int,QTY int,primary key(PNO))")



def intro():
    print()
    print("_"*85)
    print("""
                               STOCK MANAGEMENT                   {}
         
    0)EXIT
    1)VIEW STOCKS
    2)ADD PRODUCT
    3)REMOVE PRODUCT
    4)UPDATE PRODUCTS
    5)SEARCH RECORD
    6)GENERATE BILLING
    """.format(now.strftime('%d-%m-%Y %H:%M')))



def intinp(stmnt):
    y=0
    while y==0:
        try:
            x=input(stmnt)
            if bool(int(x))==True:
                y=1
                return int(x)
            if x=="0":
                y=1
                return int(x)
        except:
            print("****Integer Value Required****")


def viewproduct():
    print()
    print("-"*105)
    crsr.execute("desc product;")
    recs=crsr.fetchall()
    print(recs[0][0].ljust(7),recs[1][0].ljust(25),recs[2][0].ljust(25),recs[3][0].ljust(10),recs[4][0].ljust(10),recs[5][0].ljust(15),sep="")
    crsr.execute("select * from product;")
    recs=crsr.fetchall()
    for rec in recs:
        print(str(rec[0]).ljust(7),rec[1].ljust(25),rec[2].ljust(25),str(rec[3]).ljust(10),str(rec[4]).ljust(10),str(rec[5]).ljust(15),sep="")
    



def addproduct():
    print("ADD PRODUCT".center(85,'='))
    try:
        n=intinp("Enter no. of records to be added:")
        for w in range (n):
            try:
                pno=intinp("Enter PNO:")
                pname=input("Enter PNAME:")
                brand=input("Enter BRAND:")
                mrp=intinp("Enter MRP:")
                sellingp=intinp("Enter SELLINGP:")
                stock=intinp("Enter STOCK:")
                record=(str(pno),pname,brand,str(mrp),str(sellingp),str(stock))
                print(record)
                print()
                confirm=input("Confirm(y/n):")
                print()
                try:
                    if confirm=="y" or confirm=="Y":
                        crsr.execute("insert into product values {}".format(record))
                        crsr.execute("commit")
                        print()
                except con.errors.IntegrityError:
                    print("****DUPLICATE KEY NOT ALLOWED****")
                except con.errors.DataError:
                    print("DATA TOO LONG")
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



def removeproduct():
    print("REMOVE PRODUCT".center(85,'='))
    print("""
    MODES:
    0)EXIT
    1)PNO
    2)PNAME
    3)BRAND""")
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
                elif mod=="qty":
                    newrec=intinp("Enter NEW QTY:")
                    crsr.execute("update product set qty={} where qty={}".format(newrec,val))
                crsr.execute("commit")
                print("RECORD UPDATED")
                return
            else:
                pass
    except:
        print("_____Wrong values_____")


def updateproduct():
    print("UPDATE PRODUCT".center(85,'='))
    print("""
    0)EXIT
    1)PNO
    2)PNAME
    3)BRAND
    4)MRP
    5)SELLINGP
    6)QTY
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
            elif mod=="6" or mod=="qty" or mod=="QTY":
                z=1
                while z==1:
                    try:
                        data=intinp("Enter CURRENT QTY:")
                        if data=="0":
                            z=1
                        else:
                            z=0
                            update("qty",data)
                    except:
                        print("_____Wrong values_____")
            else:
                print("WRONG MODE SELECTED...")
        except ValueError:
            print("_____Wrong values_____")
    
            
def searchby():
    print("SEARCH PRODUCT".center(85,'='))
    print("""
    MODES:
    0)EXIT
    1)PNO
    2)PNAME
    3)BRAND
    4)QTY""")
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
                            searchrecord("pno",val)
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
                            searchrecord("pname",data)
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
                            searchrecord("brand",data)
                    except:
                        print("_____Wrong values_____")
            elif mod=="4" or mod=="qty" or mod=="QTY":
                z=1
                while z==1:
                    try:
                        val=intinp("Enter QTY:")
                        if val==0:
                            z=0
                        else:
                            searchrecord("qty",val)
                            z=0
                    except:
                        print("_____Wrong values_____")
            else:
                print("WRONG MODE SELECTED...")
        except ValueError:
            print("_____Wrong values_____")


def instock(pno,demand):
    z=1
    while z==1:
        try:
            crsr.execute("select * from product where pno={}".format(str(pno)))
            data=crsr.fetchone()
            cqty=data[5]
            if cqty==0:
                print(data[1]," IS OUT OF STOCK")
                return 0
            elif demand>cqty:
                print("Sorry,we only have",cqty)
                ch=intinp("Want to buy all?(0/1)")
                if ch==1:
                    return cqty
                else:
                    return 0
            else:
                return demand
        except Exception as err:
            print("_____Wrong values_____",err)
            
                
    
def searchrecord(by,val):
    try:
        crsr.execute("select * from product where {}='{}'".format(by,val))
        data=crsr.fetchall()
        if data==[]:
            print("EMPTY RECORD")
        else:
            crsr.execute("desc product;")
            recs=crsr.fetchall()
            print(recs[0][0].ljust(7),recs[1][0].ljust(25),recs[2][0].ljust(25),recs[3][0].ljust(10),recs[4][0].ljust(10),recs[5][0].ljust(10),sep="")
            for rec in data:
                print(str(rec[0]).ljust(7),rec[1].ljust(25),rec[2].ljust(25),str(rec[3]).ljust(10),str(rec[4]).ljust(10),recs[5][0].ljust(10),sep="")
    except:
        print("_____Wrong values_____")


def billing():
    print("BILLING".center(85,'='))
    viewproduct()
    pnolist=[]
    qtylist=[]
    y=0
    sm=0
    print("ENTER PNO AS 0 TO EXIT")
    print()
    while y==0:
        try:
            no=intinp("Enter PNO:")
            if no==0:
                sm=0
                disc=0
                tdisc=0
                smprice=0
                print("-"*85)
                crsr.execute("desc product;")
                recs=crsr.fetchall()
                print(recs[0][0].ljust(3),recs[1][0].ljust(20),recs[2][0].ljust(20),recs[3][0].ljust(7),recs[4][0].ljust(8),"PRICE".ljust(7),"DISC".ljust(4),"COST".ljust(7))
##                crsr.execute("desc product;")
##                recs=crsr.fetchall()
##                print("%3s  %-15s %-15s %4s  %-3s  %-5s %5s %5s"%(recs[0][0],recs[1][0],recs[2][0],recs[3][0],"QTY","PRICE","DISC","COST"))
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
                    print(str(rec[0]).ljust(3),rec[1].ljust(20),rec[2].ljust(20),str(rec[3]).ljust(7),str(rec[4]).ljust(8),str(rec[3]*qtylist[i]).ljust(7),str(disc).ljust(4),str(cost).ljust(7))
##                    print("%3s  %-15s %-15s %4s  %3s  %5s %5s %5s"%(rec[0],rec[1],rec[2],rec[3],qtylist[i],rec[3]*qtylist[i],disc,cost))
                print("%58s %6s"%("TOTAL PRICE:",smprice))
                print("%58s %6s"%("TOTAL DISCOUNT:",tdisc))
                print("%58s %6s"%("AMOUNT TO BE PAID:",sm))
                print('''
    0) No
    1) Yes''')
                ch=intinp("Want To Update QTY?(0/1):")
                if ch==1:
                    for i in range(len(pnolist)):
                        crsr.execute("update product set qty=qty-{} where pno={}".format(qtylist[i],pnolist[i]))
##                        qry="UPDATE PRODUCT SET QTY=QTY-{} WHERE PNO={}".format(qtylist[i],pnolist)
##                        crsr.execute(qry)
                    print("QTY UPDATED")
                    crsr.execute("commit")
                else:
                    print("QTY NOT UPDATED")
                break
                y=1
            else:
                z=0
                while z==0:    
                    amt=intinp("Enter amount:")
                    amount=instock(no,amt)
                    if amount!=0:
                        crsr.execute("select * from product where pno={}".format(no))
                        rec=crsr.fetchone()
                        if rec==None:
                            print("_____Wrong values_____")
                            z=1
    ##                      break
                        else:
                            cost=int(rec[4])*amount
                            sm=sm+cost
                            crsr.execute("desc product;")
                            recs=crsr.fetchall()
                            print(recs[0][0].ljust(3),recs[1][0].ljust(20),recs[2][0].ljust(20),recs[3][0].ljust(7),recs[4][0].ljust(8),"AMOUNT".ljust(7),"COST".ljust(7))
                            print(str(rec[0]).ljust(3),rec[1].ljust(20),rec[2].ljust(20),str(rec[3]).ljust(7),str(rec[4]).ljust(8),str(amount).ljust(7),str(cost).ljust(7))
    ##                        print("%3s %-15s %-15s %5s  %8s %5s %4s"%(recs[0][0],recs[1][0],recs[2][0],recs[3][0],recs[4][0],"QTY","COST"))
    ##                        print("%3s %-15s %-15s %5s  %8s %5s %4s"%(rec[0],rec[1],rec[2],rec[3],rec[4],qty,cost))
                            print()
                            pnolist.append(no)
                            qtylist.append(amount)
                    z=1
                    break
        except ValueError:
            print("_____Wrong values_____")


            
def main():
    dbtable()
    while True:
        time.sleep(1)
        intro()
        option=input("Enter Option:")
        if option=="1":
            viewproduct()
        elif option=="2":
            addproduct()        
        elif option=="3":
            removeproduct()
        elif option=="4":
            updateproduct()
        elif option=="5":
            searchby()
        elif option=="6":
            billing()
        elif option=="0":
            print("Thanks for using...")
            break
        else:
            print("Try Again")
main()
        
    
    
