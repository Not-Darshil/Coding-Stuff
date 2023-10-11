##define a
##function having database name d and table name t and price p as its argument .
##Display the records of table whose price is above p

##in the same function .... increase the price of the
##products by 15%  whose name begin with 'c';
import mysql.connector as con
def fx(d,t,p):
    db=con.connect(user="root",host="localhost",database=d,password="",charset="utf8")
    crsr=db.cursor()
##    crsr.execute("USE {}".format(d))
    crsr.execute("SELECT * FROM {} WHERE PRICE>{};".format(t,p))
    recs=crsr.fetchall()
    for rec in recs:
        print(str(rec[0]).ljust(5),rec[1].ljust(15),str(rec[2]).ljust(15))
    print("------------------------------------------")
    crsr.execute("UPDATE {} SET PRICE=PRICE*1.5 WHERE NAME LIKE 'c%'".format(t))
    crsr.execute("commit")
    print("completed")
fx("sample","product",100)
