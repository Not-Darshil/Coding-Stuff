import mysql.connector as con
db=con.connect(host='localhost',user='root',password='',charset='utf8',database='School')
crsr=db.cursor(buffered=True)
crsr.execute('SELECT * FROM BOOKS WHERE PRICE>50;')
x=crsr.fetchall()
for w in x:
    print('{}'.format(w[0]).ljust(5),w[1].ljust(15),'{}'.format(w[2]).ljust(15))
print('No. of Books with title that starts with P ',end='')
crsr.execute('SELECT COUNT(*) FROM BOOKS WHERE TITLE LIKE "%P%";')
x=crsr.fetchall()
for w in x:
    print(w[0])

