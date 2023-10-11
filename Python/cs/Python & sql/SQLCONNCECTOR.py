##Write a program to build a table named as stationary with attributes Id, name, price, company
##Id is primary key
##Add records until user want and display same
z=0
import mysql.connector as con
while z==0:
    try:
        pswd=input("Enter Password:")
        dbobj=con.connect(host="localhost",user="root",password=pswd,charset="utf8")
        z=1
    except:
        print("Wrong Password")
crsr=dbobj.cursor()
def db():
    crsr.execute("CREATE DATABASE IF NOT EXISTS SAMPLE;")
    crsr.execute("commit")
    crsr.execute("USE SAMPLE;")
    crsr.execute("commit")
    crsr.execute("CREATE TABLE IF NOT EXISTS STATIONARY(Id int Primary key,Name char(20),Price int,Company char(20));")
    crsr.execute("commit")
db()

def que():
    y=0
    print("Enter ID as 0 to exit")
    while y==0:
        try:
            i=int(input("Enter ID:"))
            if i==0:
                y=1
            else:    
                name=input("Enter Name:")
                price=int(input("Enter Price:"))
                company=input("Enter Company:")
                lst=(str(i),name,str(price),company)
                print(lst)
                confirm=input("Confirm(Y/N):")
                if confirm=="Y" or "y":
                    crsr.execute("INSERT INTO STATIONARY VALUES ('{}','{}','{}','{}')".format(i,name,price,company))
                    crsr.execute("commit")
        except:
            print("Some ERROR")
que()
            
            

