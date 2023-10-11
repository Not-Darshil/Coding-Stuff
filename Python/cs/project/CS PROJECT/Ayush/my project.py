import mysql.connector as c
con=c.connect(host='localhost',user='root',password='',charset='utf8')
if con.is_connected():

    print('Successfully connected')

cursor=con.cursor()
def dbtable():
    cursor.execute('create database if not exists final_proj')
    cursor.execute('use final_proj')
    cursor.execute('create table if not exists student(Rno int primary key,Name char(15),Class varchar(50)\
,Sec varchar(50),Gender varchar(50))')
    cursor.execute('create table if not exists teacher(Id int primary key,Name char(15),Join_date varchar(50)\
,Subj varchar(50),Post varchar(50))')
    

dbtable()

def main_menu():
    while True:
        print('_'*83)
        print('''
                                                                      ABC Public School
                                                            Enter 0 for Exit 
                                                            Enter 1 for Viewing Students Details
                                                            Enter 2 for Viewing Teachers Details''')
        print('_'*83)        
        choice=int(input('Enter here(0-2):-'))
        if choice==0:
            break
        elif choice==1:
            student_menu()
        elif choice==2:
            teacher_menu()
        elif choice==3:
            schl_menu()
        else:
            print('Wrong choice..............')
    print('Programm End.........\nThank You')

def student_menu():
    while True:
        print('_'*83)
        print('''
                                                                 _STUDENT DETAILS_
                                                             Enter 0 for Exit
                                                             Enter 1 for Entering New record
                                                             Enter 2 for Updating Details
                                                             Enter 3 for Deleting Records
                                                             Enter 4 for Displaying Records ''')
        print('_'*83)       
        ch1=int(input('Enter your choice here(0-4) :- '))
        if ch1==0:
            break
        if ch1==1:        
            st_newrec()
        elif ch1==2:
            st_upd()
        elif ch1==3:
            st_del()
        elif ch1==4:
            st_show()
        else:
            print('Wrong choice............')


def st_newrec():
    try:
        con=c.connect(host='localhost',user='root',password='',database='final_proj',charset='utf8')
        cursor=con.cursor()
        print('''
                                                            ENTERING THE NEW RECORD''')
        ch=int(input('''
Enter the number of rec you want to add
Please Enter Here : '''))
        for w in range(1,ch+1):
            print()
            print('[Entering the',w,'record]')
            print()
            rno=int(input('Enter the rno of the student : '))
            name = input('Enter the name of the student : ')
            Class=int(input('Enter the class of the student : '))
            gender=input('Enter the Gender of the student : ')
            sec=input('Enter the section of the student : ')
            
            query='Insert into student values({},"{}",{},"{}","{}")'.format(rno,name,Class,sec,gender)
            cursor.execute(query)
        con.commit()
        con.close()
        print('Record is succesfully inserted........')
        print()

    except Exception as error:
        print('ERROR :- ',error)

def st_upd():
        try:
            con=c.connect(host='localhost',user='root',password='',database='final_proj',charset='utf8')
            cursor=con.cursor()
            print('''
                                                            UPDATING THE RECORD''')
            choice=int(input('Enter the number of records u want to update : '))
            for w in range (1,choice+1):
                print()
                rno=int(input('Enter the roll number of the student for updating the records : - '))
                print()
                print('''
    Enter 1 for updating Name
    Enter 2 for updating Class
    Enter 3 for updating Gender
    Enter 4 for updating Section''')
                print()
                choice=int(input('Enter Here:-'))
                if choice==1:
                    nw_nme=input('Enter correct name : ')
                    cursor.execute('update student set name="%s" where rno=%d'%(nw_nme,rno))
                    con.commit()
                    print('Record updated........')
                elif choice==2:
                    nw_class=int(input('Enter the correct class : '))
                    cursor.execute('update student set class=%d where rno=%d'%(nw_class,rno))
                    con.commit()
                    print('Record updated........')
                elif choice==3:
                    nw_gender=input('Enter the correct Gender of the student : ')
                    cursor.execute('update student set gender="%s" where rno=%d'%(nw_gender,rno))
                    con.commit()
                    print('Record updated.........')
                elif choice==4:
                    nw_sec=input('Enter correct Section')
                    cursor.execute('update student set sec="%s" where rno=%d'%(nw_sec,rno))
                    con.commit()
                    print('Record updated........')
                else:
                    print('WRONG CHOICE !!!!!!!!')
            con.close()
            print()
        except Exception as error:
            print('ERROR :- ',error)

def st_del():
    try:
        con=c.connect(host='localhost',user='root',password='',database='final_proj',charset='utf8')
        cursor=con.cursor()
        print('''
                                                            DELETING THE RECORD''')
        choice=int(input('''
Enter 1 for deleting all the records
Enter 2 for deleting specific number of records
ENTER HERE : '''))
        if choice==1:
            que='Delete from student'
            cursor.execute(que)
        elif choice==2:
            ch2=int(input('''
Enter the number of records u want to delete : '''))
            for w in range(1,ch2+1):
                print()
                rn=int(input('Enter the Roll num Here : '))
                print()
                query='delete from student where rno={}'.format(rn)
                cursor.execute(query)
        else:
            print('----------------Please enter according to instructions----------------')
            del_rec()
        con.commit()
        con.close()
        print('Record deleted completely...........')
        print()
    except Exception as error:
        print('Errorc :- ',error)
      
def st_show():
    try:
        con=c.connect(host='localhost',user='root',password='',database='final_proj',charset='utf8')
        cursor=con.cursor()
        print('''
                                                            DISPLAYING THE STUDENTS RECORD''')
        cursor.execute('desc student')
        recs=cursor.fetchall()
        print(recs[0][0].ljust(6),recs[1][0].ljust(20),recs[2][0].ljust(10),recs[3][0].ljust(10),recs[4][0].ljust(10),\
              sep='')
        Que='select * from student'
        cursor.execute(Que)
        w=cursor.fetchall()  
        for rec in w:
            print(str(rec[0]).ljust(8),rec[1].ljust(20),str(rec[2]).ljust(10),rec[3].ljust(10),rec[4].ljust(10),sep='')
        con.commit()
        con.close()
        print()
    except Exception as error:
        print('Error :- ',error)

def teacher_menu():
    while True: 
        print('='*89)
        print('''
                                                                TEACHER DETAILS
                                                                Enter 0 for Exit
                                                                Enter 1 for Inserting new record
                                                                Enter 2 for Updating Existing record
                                                                Enter 3 for Deleting the records
                                                                Enter 4 for Displaying the records''')
        print('='*89)       
        choice=int(input('Enter here (0-4): '))
        if choice==0:
            break
        elif choice==1:
            new_rec()
        elif choice==2:
            upd_rec()
        elif choice==3:
            del_rec()
        elif choice==4:
            show_rec()
        else:
            print('Wrong Entry................')

def new_rec():
    try:
        con=c.connect(host='localhost',user='root',password='',database='final_proj',charset='utf8')
        cursor=con.cursor()
        print('''
                                                            ENTERING THE NEW RECORD''')
        ch=int(input('''
Enter the number of rec you want to add
Please Enter Here : '''))
        for w in range(1,ch+1):
            print()
            print('[Entering the',w,'record]')
            print()
            Id=int(input('Enter the Id of the Teacher : '))
            name = input('Enter the Name of the Teacher : ')
            j_date=input('Enter the Joning date(DD-MM-YYYY) : ')
            sub=input('Enter the Subject of the Teacher : ')
            post=input('Enter the Post of the teacher : ')
            query='Insert into teacher values({},"{}","{}","{}","{}")'.format(Id,name,j_date,sub,post)
            cursor.execute(query)
        con.commit()
        con.close()
        print('Record is succesfully inserted........')
        print()

    except Exception as error:
        print('ERROR :- ',error)
        
def upd_rec():
    try:
        con=c.connect(host='localhost',user='root',password='',database='final_proj',charset='utf8')
        cursor=con.cursor()
        print('''
                                                            UPDATING THE RECORD''')
        ch=int(input('Enter the number of rec you want to update :- '))
        for w in range(1,ch+1):
            Id=int(input('Enter the Id of  Teacher for updating the records : - '))
            print()
            print('''
    Enter 1 for updating Name
    Enter 2 for updating Doj
    Enter 3 for updating sub
    Enter 4 for updating Post''')
            print()
            choice=int(input('Enter Here:-'))
            if choice==1:
                nme=input('Enter correct Name : ')
                cursor.execute('update teacher set name="%s" where id=%d'%(nme,Id))
                con.commit()
                print('Record updated')
            elif choice==2:
                doj=int(input('Enter the correct DOJ : '))
                cursor.execute('update teacher set join_date="%s" where id=%d'%(doj,Id))
                con.commit()
                print('Record updated')
            elif choice==3:
                sub=input('Enter the correct Subject of the Teacher : ')
                cursor.execute('update teacher set subj="%s" where id=%d'%(sub,Id))
                con.commit()
                print('Record updated')
            elif choice==4:
                post=input('Enter correct Post of teacher : ')
                cursor.execute('update teacher set post="%s" where id=%d'%(post,Id))
                con.commit()
                print('Record updated')
            else:
                print('WRONG CHOICE')
            con.close()
        print()
    except Exception as error:
        print('ERROR :- ',error)
    
def del_rec():
    try:
        con=c.connect(host='localhost',user='root',password='',database='final_proj',charset='utf8')
        cursor=con.cursor()
        print('''
                                                            DELETING THE RECORD''')
        choice=int(input('''
Enter 1 for deleting all the records
Enter 2 for deleting specific number of records
ENTER HERE : '''))
        if choice==1:
            que='Delete from teacher'
            cursor.execute(que)
        elif choice==2:
            ch2=int(input('''
Enter the number of records u want to delete : '''))
            for w in range(1,ch2+1):
                print()
                rn=int(input('Enter the Id Here : '))
                query='delete from teacher where ID={}'.format(rn)
                cursor.execute(query)
        else:
            print('----------------Please enter according to instructions----------------')
            del_rec()
        con.commit()
        con.close()
        print('Record deleted completely...........')
        print()
    except Exception as error:
        print('Error :- ',error)
    
def show_rec():
    try:
        con=c.connect(host='localhost',user='root',password='',database='final_proj',charset='utf8')
        cursor=con.cursor()
        print('''
                                                    DISPLAYING THE TEACHERS RECORD''')
        cursor.execute('desc teacher')
        data=cursor.fetchall()
        print(data[0][0].ljust(6),data[1][0].ljust(22),data[2][0].ljust(20),data[3][0].ljust(20),data[4][0].ljust(20),\
              sep='')
        Que='select * from teacher'
        cursor.execute(Que)
        w=cursor.fetchall()
        for rec in w:
            print(str(rec[0]).ljust(7),rec[1].ljust(20),rec[2].ljust(18),rec[3].ljust(20),rec[4].ljust(10),sep='')
        con.commit()
        con.close()
        print()
    except Exception as error:
        print('Error :- ',error)
        
def pswd():
    pwd=input('Enter Password :- ')
    if pwd=='1269':
        main_menu()
    else:
        print('Oops Wrong Password............')
        pswd()
pswd()




