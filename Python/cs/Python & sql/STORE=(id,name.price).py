##Q
##Define a function having a nested list as it's argument having Id, name, price.
##Write these records on table item present in database STORE
import mysql.connector as con
db=con.connect(host="localhost",password="",user="root",charset="utf8",database="store")
crsr=db.cursor()
crsr.execute("create table item ('ID' varchar(),'Name',varchar(),'Price' int ,primary key ID);")
k=[]
while True:
    i=input("Enter ID:")
    name=input("Enter NAME:")
    price=int(input("Enter Price:"))
    k.append([i,name,price])
def fx(lst):
    for w in lst:
        crsr.execute("INSERT INTO ITEM('{}','{}',{})".format(w[0],w[1],w[2]))
crsr.commit()
