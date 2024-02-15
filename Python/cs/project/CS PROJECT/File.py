def push(stack, item):
    stack.append(item)
## Stack-2
##def pop(stack):
##    if stack==[]:
##        return
##    return stack.pop()
##def oddStack(num):
##    if num%2==1:
##        push(stack,num)
##def GetLargest(stack):
##    elem=pop(stack)
##    large=elem
##    while elem!=None:
##        if large<elem:
##            large=elem
##        elem=pop(stack)
##    return large
##n=int(input("how many numbers? "))
##stack=[] #empty stack
##large= -99
##for i in range(n):
##    number=int(input("Enter number: "))
##    oddStack(number)
##print("Stack created is ", stack)
##large=GetLargest(stack)
##print("Largest number in stack",large)



## def PushS(lst):
##    n= int(input("Enter integer:"))
##    lst.append(n)
##def PopS(lst):
##    if lst==[]:
##        print("Stack is empty--UNDERFLOW!")
##    else:
##        print ("Deleted value :",lst.pop())
##lst=[]
##while True:
##    print("""
##1)PUSH
##2POP
##3)EXIT
##""")
##    ch=int(input("Enter Option:"))
##    if ch==1:
##        PushS(lst)
##    elif ch==2:
##        PopS(lst)
##    elif ch==3:
##        break
##    else:
##        print("Wrong Option")
##

##q Q. Write a menu driven program that has functions Make Push (package) and
##MakePop(package) to add a new Package and delete & Package from a List of Package
##Description, considering them to act as push and pop operations of the Stack
##def MakePush(package):
##    a = int(input("Enter package title: "))
##    package.append(a)
##def MakePop(package):
##    if package==[]:
##        print("Stack empty")
##    else:
##        print ("Deleted element:",package.pop())
##package=[]
##while True:
##    print("""
##1)PUSH
##2)POP
##3)EXIT
##""")
##    ch=int(input("Enter Option:"))
##    if ch==1:
##        MakePush(package)
##    elif ch==2:
##        MakePop(package)
##    elif ch==3:
##        break
##    else:
##        print("Wrong Option")

##Write a program to implement a stack for these book-details(Bookno, book name). That is now
##each item node of the stack contains two types of information-a bookno and its name.
####Just implement Push and display operations.
##
##def Push(stk,item):
##    stk.append(item)
##    top=len(stk)-1
##def Display(stk):
##    if stk==[]:
##        print("Stack empty")
##    else:
##        top=len(stk)-1
##        print(stk[top],"<-top")
##        for a in range(-2,-top-2, -1):
##            print(stk[a])
##        
##stack=[]
##top=None
##while True:
##    print("STACK OPERATIONS")
##    print("1. Push")
##    print("2. Display stack")
##    print("3. Exit")
##    ch=int(input("Enter your choice (1-5) :"))
##    if ch==1:
##        bno=int(input("Enter Book no. to be inserted :"))
##        bname=input("Enter Book name to be inserted :") 
##        item=[bno, bname]
##        Push(stack,item)
##    elif ch==2:
##        Display(stack)
##    elif ch==3:
##        break
##    else:
##        print("Invalid choice!")



####Write a program to perform insert and delete operations on a Queue containing Members
####details as given in the following definition of itemnode:
####
####MemberNo
####integer
####MemberName String
####Age
####solution
####integer
##def isEmpty(Qu):
##    if Qu==[]:
##        return True
##    else :
##        return False
##    
##def Enqueue(Qu,item):
##    Qu.append(item)
##    if len(Qu)==1:
##        front=rear = 0
##    else:
##        rear=len(Qu) - 1
##        
##def Dequeue(Qu):
##    if isEmpty(Qu) :
##        return "Underflow"
##    else:
##        item= Qu.pop(0)
##        if len(Qu) == 8:
##            front=None
##            rear=None
##        return item
##def Display(Qu):
##    if isEmpty(Qu):
##        print("Queue Empty!")
##    elif len(Qu)==1:
##        print(Qu[0], "<== front, rear")
##    else:
##        front=0
##        rear=len(Qu)-1
##        print(Qu[front],"<--front")
##        for a in range(1, rear):
##            print (Qu[a])
##        print (Qu[rear], "<-rear")
##queue=[]
##front=None
##while True:
##    print("QUEUE OPERATIONS")
##    print("1. Enqueue")
##    print("2. Dequeue")
##    print("3. Display queue")
##    print("4. Exit")
##    ch= int(input("Enter your choice (1-5): "))
##    if ch==1:
##        print("For the new member, enter details below:")
##        memberNo= int(input("Enter member no :"))
##        memberName=input("Enter member name :")
##        age = int(input("Enter member's age :"))
##        item=[memberNo,memberName,age]
##        Enqueue(queue,item)
##        input("Press Enter to continue...")
##    elif ch==2:
##        item=Dequeue(queue)
##        if item=="Underflow":
##            print("Underflow! Queue is empty!")
##        else:
##            print("Dequeue-ed item is", item)
##            input("Press Enter to continue...")
##    elif ch==3:
##        Display (queue)
##        input("Press Enter to continue...")
##    elif ch == 4:
##        break
##    else :
##        print("Invalid choice!")
##        input("Press Enter to continue...")


##Write a function in Python,INSERTQ(arr,data) and DELETEQ(Arr) for performing
##insertion and deletion operations in a Queue. arr is the list used for implementing
##queue and data is the value to be inserted.



##def INSERTQ(arr):
##    data =int(input("Enter data to be inserted: "))
##    arr.append(data)
##
##def DELETEQ(arr):
##    if arr== []:
##        print("Queue empty")
##    else:
##        print ("Deleted element is:", arr[0])
##        arr.pop(0)
##arr=[]
##while True:
##    print("""
##1)INSERTQ
##2)DELETEQ
##3)EXIT
##""")
##    ch=int(input("Enter Option:"))
##    if ch==1:
##        INSERTQ(arr)
##    elif ch==2:
##        DELETEQ(arr)
##    elif ch==3:
##        break
##    else:
##        print("Wrong Option")

##
##import mysql.connector as c
##con=c.connect(host='localhost',user='root',password='',database='school',charset='utf8')
##if con.is_connected():
##    print('succesfully connected..........')
##cursor=con.cursor()
##print()
##print('Records of the student of section A :- ')
##print()
##cursor.execute('desc class_12')
##recs=cursor.fetchall()
##print(recs[0][0].ljust(8),recs[1][0].ljust(20),recs[2][0].ljust(10),recs[3][0].ljust(10),recs[4][0].ljust(10),\
##      sep='')
##que='select * from class_12 where sec="A" '
##cursor.execute(que)
##dat=cursor.fetchall()
##for rec in dat:
##    print(str(rec[0]).ljust(8),rec[1].ljust(20),str(rec[2]).ljust(10),rec[3].ljust(10),rec[4].ljust(10),sep='')
##
##dat=cursor.fetchall()

##import mysql.connector as c
##con=c.connect(host='localhost',user='root',password='',database='school',charset='utf8')
##if con.is_connected():
##    print('succesfully connected..........')
##cursor=con.cursor()
##
##def display():
##    try:
##        cursor.execute('desc class_12')
##        recs=cursor.fetchall()
##        print(recs[0][0].ljust(6),recs[1][0].ljust(15),recs[2][0].ljust(10),recs[3][0].ljust(10),recs[4][0].ljust(10),\
##              sep='')
##        Que='select * from class_12'
##        cursor.execute(Que)
##        w=cursor.fetchall()  
##        for rec in w:
##            print(str(rec[0]).ljust(8),rec[1].ljust(20),str(rec[2]).ljust(10),rec[3].ljust(10),rec[4].ljust(10),sep='')
##    except Exception as error:
##        print('Error :- ',error)

##import mysql.connector as c
##con=c.connect(host='localhost',user='root',password='',database='school',charset='utf8')
##if con.is_connected():
##    print('succesfully connected..........')
##cursor=con.cursor()
##def delete():
##    while True:
##        print('''
##    1)Delete all
##    2)Delete with Rno
##    3)Exit''')
##        ch=int(input("Enter Choice:"))
##        if ch==1:
##            que='Delete from class_12'
##            cursor.execute(que)
##        elif ch==2:
##            rn=int(input('Enter Roll number: '))
##            query='delete from class_12 where rno={}'.format(rn)
##            cursor.execute(query)
##        elif ch==3:
##            break
##        else:
##            print('WRONG CHOICE.....')
##        con.commit()
##        print('Record deleted ...........')
##delete()


##import mysql.connector as c
##con=c.connect(host='localhost',user='root',password='',charset='utf8')
##if con.is_connected():
##    print('succesfully connected..........')
##cursor=con.cursor()
##
##def db():
##    que='create database if not exists school'
##    cursor.execute(que)
##    print('Database created...')
##db()

##import mysql.connector as c
##con=c.connect(host='localhost',user='root',password='',database='school',charset='utf8')
##if con.is_connected():
##    print('succesfully connected..........')
##cursor=con.cursor()
##
##def tb():
##    cursor.execute('create table if not exists class_12(Rno int primary key,Name varchar(15),Class int,Sec varchar(10),Gender varchar(15))')
##print('Table is created...')
##tb()


##import mysql.connector as c
##con=c.connect(host='localhost',user='root',password='',database='school',charset='utf8')
##if con.is_connected():
##    print('succesfully connected..........')
##cursor=con.cursor()
##
##def insert():
##    try:
##        for w in range(3):
##            print()
##            print('Entering the',w+1,'record')
##            rno=int(input('Enter rno: '))
##            name = input('Enter name:')
##            Class=int(input('Enter class:'))
##            sec=input('Enter section:')
##            gender=input('Enter Gender: ')
##            query='Insert into class_12 values({},"{}",{},"{}","{}")'.format(rno,name,Class,sec,gender)
##            cursor.execute(query)
##        con.commit()
##        con.close()
##        print('Record is succesfully inserted........')
##        
##    except:
##        print("Some Error")
##insert()


##import mysql.connector as c
##con=c.connect(host='localhost',user='root',password='',database='school',charset='utf8')
##if con.is_connected():
##    print('succesfully connected..........')
##cursor=con.cursor()
##def update():
##    rno=int(input('Enter roll number:'))
##    cursor.execute('desc class_12')
##    recs=cursor.fetchall()
##    print(recs[0][0].ljust(8),recs[1][0].ljust(20),recs[2][0].ljust(10),recs[3][0].ljust(10),recs[4][0].ljust(10),sep='')
##    cursor.execute('select * from class_12 where rno={}'.format(rno))
##    w=cursor.fetchall()  
##    for rec in w:
##        print(str(rec[0]).ljust(8),rec[1].ljust(20),str(rec[2]).ljust(10),rec[3].ljust(10),rec[4].ljust(10),sep='')
##    print('''
##    1)Name
##    2)Class
##    3)Gender
##    4)Section''')
##    print()
##    ch=int(input('Enter Here:'))
##    if ch==1:
##        name=input('Enter new name :')
##        cursor.execute('update class_12 set name="%s" where rno=%d'%(name,rno))
##        con.commit()
##        print('Record updated........')
##    elif ch==2:
##        clas=int(input('Enter new class :'))
##        cursor.execute('update class_12 set class=%d where rno=%d'%(clas,rno))
##        con.commit()
##        print('Record updated........')
##    elif ch==3:
##        gender=input('Enter the new Gender :')
##        cursor.execute('update class_12 set gender="%s" where rno=%d'%(gender,rno))
##        con.commit()
##        print('Record updated.........')
##    elif ch==4:
##        sec=input('Enter new Section :')
##        cursor.execute('update class_12 set sec="%s" where rno=%d'%(sec,rno))
##        con.commit()
##        print('Record updated........')
##    else:
##        print('WRONG CHOICE !!!!!!!!')
##    con.close()
##update()


##import mysql.connector as c
##con=c.connect(host='localhost',user='root',password='',database='school',charset='utf8')
##if con.is_connected():
##    print('succesfully connected..........')
##cursor=con.cursor()
##print()
##que='delete from class_12 where sec="A" '
##cursor.execute(que)
##con.commit()
##cursor.execute('desc class_12')
##recs=cursor.fetchall()
##print(recs[0][0].ljust(6),recs[1][0].ljust(20),recs[2][0].ljust(10),recs[3][0].ljust(10),recs[4][0].ljust(10),sep='')
##que='select * from class_12 '
##cursor.execute(que)
##dat=cursor.fetchall()
##for rec in dat:
##    print(str(rec[0]).ljust(6),rec[1].ljust(20),str(rec[2]).ljust(10),rec[3].ljust(10),rec[4].ljust(10),sep='')


##import mysql.connector as c
##con=c.connect(host='localhost',user='root',password='',database='school',charset='utf8')
##if con.is_connected():
##    print('succesfully connected..........')
##crsr=con.cursor()
##print()
##crsr.execute('desc class_12')
##recs=crsr.fetchall()
##print(recs[0][0].ljust(6),recs[1][0].ljust(20),recs[2][0].ljust(10),recs[3][0].ljust(10),recs[4][0].ljust(10),sep='')
##que='select * from class_12 '
##crsr.execute(que)
##dat=crsr.fetchmany(3)
##for rec in dat:
##    print(str(rec[0]).ljust(6),rec[1].ljust(20),str(rec[2]).ljust(10),rec[3].ljust(10),rec[4].ljust(10),sep='')
##con.close()

##
##import mysql.connector as c
##con=c.connect(host='localhost',user='root',password='',database='school',charset='utf8')
##if con.is_connected():
##    print('succesfully connected')
##cursor=con.cursor()
##que='delete from class_12 where gender="Male" '
##cursor.execute(que)
##con.commit()
##print('DISPLAYING THE RECORDS……')
##print()
##cursor.execute('desc class_12')
##recs=cursor.fetchall()
##print(recs[0][0].ljust(8),recs[1][0].ljust(20),recs[2][0].ljust(10),recs[3][0].ljust(10),recs[4][0].ljust(10),sep='')
##Que='select * from class_12'
##cursor.execute(Que)
##w=cursor.fetchall()  
##for rec in w:
##    print(str(rec[0]).ljust(8),rec[1].ljust(20),str(rec[2]).ljust(10),rec[3].ljust(10),rec[4].ljust(10),sep='')

import mysql.connector as c
con=c.connect(host='localhost',user='root',password='',database='sample',charset='utf8')
if con.is_connected():
    print('Successfully connected')       
cursor=con.cursor()
print('Displaying records before deleting..............')
cursor.execute('select*from stationary')
data=cursor.fetchall()
for a in data:
    print(a)
nme=input('Enter the name for deleting the record :-')
que='delete from stationary where name="%s"'%(nme)
cursor.execute(que)
print()
cursor.execute('select*from stationary')
data=cursor.fetchall()
print('Displaying records after deleting.......')
for w in data :
    print(w)
con.commit()
con.close()
print('Record deleted completely.......')

        
input()



