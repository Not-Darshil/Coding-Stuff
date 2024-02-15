import mysql.connector as sql

db=sql.connect(host='localhost',user='root',password='vivek',charset='utf8')
c=db.cursor(buffered=True)
def create_database(name):
    cr=db.cursor(buffered=True)
    cr.execute("create database if not exists {}".format(name))
def use_database(database_name):
    cr = db.cursor(buffered=True)
    cr.execute("use {}".format(database_name))
def create_table(table_name,attributes):
     cr=db.cursor(buffered=True)


     qry='create table if not exists {}{}'.format(table_name,attributes)
     cr.execute(qry)
def details():
        create_table('Participants', '(Name varchar(30),mob varchar(13),email varchar(20),dob date,grade varchar(3))')

        detail_status=False
        while detail_status==False:

            name=input('Name : ')

            mob=input('Mobile no : ')
            email=input('E-mail : ')

            dob=input('DOB (yyyy-mm-dd) : ')
            grade=input("Grade: ")
            details= (name,mob,email,dob,grade)

            try:
                data_insertion('Participants',details)
                print("Data inserted successfully")
                detail_status=True
            except Exception as e:
                print(e)
                print("Please enter correct data")
        return name[:4]+dob[:4]
def data_insertion(table_name,data_list):
    cr=db.cursor(buffered=True)
    cr.execute(f"insert into {table_name} values{data_list}")
    cr.execute('commit')
def category(list):
    create_table('Category','(sno int primary key,categories varchar(20))')
    for items in list:
        # print(items)
        data_insertion('Category',items)
def show_category():
    c.execute('select * from category')
    data=c.fetchall()
    print('%-5s %20s' % ('sno', 'categories'))
    for sno,category in data:
        print('%2s %30s'%(sno,category))
def question(table_name,questions):
    create_table(table_name,'(q_id varchar(4) primary key,questions varchar(60),A varchar(20),B varchar(20),C varchar(20),D varchar(20))')
    try:
        for question in questions:
            data_insertion(table_name,question)
    except:
        pass
def answer(answers):
    create_table('answer','(q_id varchar(5) primary key,correct_option varchar(20))')
    for ans in answers:
        try:
            data_insertion('answer',ans)
        except:
            pass
def show_question(table_name,id):
    c.execute(f"select * from {table_name} where q_id='{id}'")
    data=c.fetchall()
    for que in data:
        print('%-4s %30s \n    a.%-10s b.%-10s c.%-10s d.%-10s'%(que[0][1:],que[1],que[2],que[3],que[4],que[5]))
def user_ans_table(user_name,ans_list):
    create_table(user_name,'(a_id varchar(5) primary key,answer varchar(20))')
    for ans in ans_list:
        try:
            data_insertion(user_name,ans)
        except:
            # print('you have submitted')
            pass
def check(ans_table,user_ans_table):
        c.execute(f'select q_id,correct_option,answer from {ans_table},{user_ans_table} where {ans_table}.q_id={user_ans_table}.a_id')
        data=c.fetchall()
        # print(data)
        marks=0
        for record in data:
            # print(record)
            if record[1].lower()==record[2].lower():
                marks+=1

        return marks
create_database('Online_Test')
use_database('online_test')
# category([(1,'String_formatting'),(2,"List_manipulation"),(3,"tuple"),(4,"Dictionary"),(5,'Sql')])

s1=('s1','function to check the is in lowercase','islower()','isupper()','isnumeric()','isdigit()')
s2=('s2','function to change in uppercase','isupper()','str.upper()','str.lower()','str.islower()')
s3=('s3','output of the code: \n print("2+4")','6','24','2+4','none of the above')
s4=('s4','function to check if there digit in string','str.isdigit()','str.isnumber()','str.islower()','none of the above')
s5=('s5','output of the code: \n print(type(23,))','(class "int")','(class "str")','(class "list")','(class "tuple")')
que=[s1,s2,s3,s4,s5]
ans=[('s1','a'),('s2','b'),('s3','c'),('s4','a'),('s5','d')]
question('questions',que)
answer(ans)
# show_question('questions','s1')
if __name__ == '__main__':


    print('Welcome to online quiz')
    print('Please Enter your details')
    name=details()

    print('Press Enter to continue')
    input()
    # print('select 2 categories out of 5')
    # show_category()
    # category_selected=input('enter category number separated by comma:  ').split(',')
    # print(category_selected)
    ans_dic={}
    for i in range(1,6):
        show_question('questions','s'+str(i))
        print()
        a=input('enter option :>> ')
        ans_dic['s'+str(i)]=a


    user_ans=list(ans_dic.items())
##    for key,value in ans_dic.items():
##
##        user_ans.append((key,value))

    user_ans_table(name,user_ans)
    mark=check('answer',name)
    print(f'you scored : {mark}')











# create_database('quiz')
#
# use_database('quiz')
# #
# # details()
# # # category([(1,'string'),(2,'list'),(3,'tuple')])
# # show_category()
# #
#
# a=('s1','function to check the is in lowercase','islower()','isupper()','isnumeric()','isdigit()')
# b=('s2','function to change in uppercase','isupper()','str.upper()','str.lower()','str.islower()')
# # question('string_formatting',(a,b))
#
# ans=(('s1','a'),('s2','b'))
# # answer(ans)
# user_ans_table('kumar1',ans)
# a=check('answer','kumar1')
# print(a)
#
# # #
# # # #
# # # c.execute("insert into category values('stringf')")
# # # c.execute('commit')
# # # data_insertion('category','kumar')
# # # field=()
# #
# # a=details()
# # print(str(a))
# # print(a)
# # # create_table('details','(name varchar(20),mob int(12))')
# # # data_insertion('details',a)
#
#
# # create_table("stu",'(name varchar(30),mob int(20),gender char(2))')
