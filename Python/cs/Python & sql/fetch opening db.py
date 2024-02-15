import mysql.connector as con
dbobj=con.connect(host="localhost",user="root",password="123456",database='db',charset='utf8')
crsr=dbobj.cursor()
##x=crsr.fetchall()
##for w in x:
##    print(w)
crsr.execute("desc stu")
x=crsr.fetchall()
print(x)
print("%8s%10s%8s"%(x[0][0],x[1][0],x[2][0]),end="\n")
print("cnt",crsr.rowcount)#3
crsr.execute("select * from stu")
x=crsr.fetchall()
for w in x:
    print("%8s%10s%8s"%(w[0],w[1],w[2]))
print("cnt",crsr.rowcount)#7

'''
x=crsr.fetchall()
print(x)
'''
'''list of tuples (tuple ka first element heading rkta h) '''


###next file me
'''creating a table using python input from the user'''




