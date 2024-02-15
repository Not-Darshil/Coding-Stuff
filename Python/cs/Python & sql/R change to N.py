def fx(r,n):
    import mysql.connector as con
    db=con.connect(user="root",host="localhost",database="school",password="",charset="utf8")
    crsr=db.cursor()
    crsr.execute("SELECT NAME FROM STUDENT")
    recs=crsr.fetchall()
    z=0
    for w in recs:
        if w[0]==r:
            crsr.execute("UPDATE STUDENT SET NAME='{}' WHERE NAME='{}'".format(r,n))
            z=z+1
    if z==0:
        print("ERROR ---NO SUCH RECORD")
    else:
        print("Records updated ")
        print("No. of columns affected:",z)

fx("Mohit","Suresh")
        
    
