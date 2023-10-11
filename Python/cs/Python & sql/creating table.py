import mysql.connector as con
dbobj=con.connect(host="localhost",user="root",password="123456",database="db")
crsr=dbobj.cursor()
if dbobj.is_connected():
    print("Connection done")
else:
    print("Connection not done")
crsr.execute("create table if not exists itemlist")

