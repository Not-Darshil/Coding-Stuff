##Q1
##def interest(principal,time=2,rate=0.10):
##  return principal*rate*time
###__main__
##Prin = float(input('Enter principal amount:'))
##print("Simple interest with default ROI and time value is:")
##Si1=interest(Prin)
##print("Rs.",Si1)
##Roi=float(input("Enter rate of interest:"))
##time=int(input("Enter time in years:"))
##print("Simple interest with your provided ROI and time value is:")
##Si2 = interest(Prin,time,Roi)
##print("Rs.",Si2)



##Q2
##test_dict = {"NEWS" : [5, 7, 5, 4, 5],
##             "PAPER" : [6, 7, 4, 3, 3], 
##             "TEST" : [9, 9, 6, 5, 5]}
##print("The original dictionary is : " + str(test_dict))
##max_val=0
##max_key=None 
##for sub in test_dict:
##    if len(set(test_dict[sub])) > max_val:
##        max_val = len(set(test_dict[sub]))
##        max_key = sub 
##print("Key with maximum unique values : " + str(max_key))


##Q3
##import mysql.connector as con
##c=con.connect(host="localhost",user="root",passwd="123456",database="supermarket") 
##if c.is_connected() == False: 
##    print('Error connecting to MySQL database') 
##crsr=c.cursor() 
##crsr.execute("select * from product") 
##data=crsr.fetchmany(3) 
##count=crsr.rowcount
##for row in data :
##    print(row) 
##c.close()





##Q4
##def pallindrome(string):
##    newstr=""
##    for w in range (-1,-len(string)-1,-1):
##        newstr=newstr+string[w]
##    if newstr==string:
##        print(string,"is a pallindrome")
##    else:
##        print(string,"is not a pallindrome")
##var=input("Enter String:")
##pallindrome(var)
##print()
##var=input("Enter String:")
##pallindrome(var)

##Q5
##def armstrong():
##    num=int(input("Enter a 3 digit number:")) 
##    su=0 
##    for w in str(num):
##        su=su+int(w)**3
##    if num==su: 
##        print(num,"is an Armstrong number") 
##    else: 
##        print(num,"is not an Armstrong number")
##armstrong()
##print()
##armstrong()


##Q6
##n=5 #for number of lines 
### upper half 
##for i in range(1,n+1):
##    print("  "," "*(n-i)+"* "*i)
### lower half 
##for i in range(n,0,-1):
##    print("  "," "*(n-i)+"* "*i)
##



##Q7
##z=0
##import mysql.connector as con
##while z==0:
##    try:
##        pswd=input("Enter Password:")
##        dbobj=con.connect(host="localhost",user="root",password=pswd,charset="utf8")
##        z=1
##    except:
##        print("Wrong Password")
##crsr=dbobj.cursor()
##def db():
##    crsr.execute("CREATE DATABASE IF NOT EXISTS SAMPLE;")
##    crsr.execute("commit")
##    crsr.execute("USE SAMPLE;")
##    crsr.execute("commit")
##    crsr.execute("CREATE TABLE IF NOT EXISTS STATIONARY(Id int Primary key,Name char(20),Price int,Company char(20));")
##    crsr.execute("commit")
##db()
##
##def que():
##    y=0
##    print("Enter ID as 0 to exit")
##    while y==0:
##        try:
##            i=int(input("Enter ID:"))
##            if i==0:
##                y=1
##            else:    
##                name=input("Enter Name:")
##                price=int(input("Enter Price:"))
##                company=input("Enter Company:")
##                lst=(str(i),name,str(price),company)
##                print(lst)
##                confirm=input("Confirm(Y/N):")
##                if confirm=="Y" or "y":
##                    crsr.execute("INSERT INTO STATIONARY VALUES ('{}','{}','{}','{}')".format(i,name,price,company))
##                    crsr.execute("commit")
##        except:
##            print("Some ERROR")
##def dis():
##    print()
##    print("-"*85)
##    crsr.execute("DESC STATIONARY;")
##    recs=crsr.fetchall()
##    print("%3s %-10s  %-5s %5s"%(recs[0][0],recs[1][0],recs[2][0],recs[3][0]))
##    crsr.execute("select * from STATIONARY;")
##    recs=crsr.fetchall()
##    for rec in recs:
##        print("%3s %-10s  %5s %5s"%(rec[0],rec[1],rec[2],rec[3]))
##que()
##dis()


##Q8
##lst=eval(input("Enter list:"))
##lstc=list(lst)
##uniq=[] 
##dupl=[] 
##for element in lst:
##    c=0
##    for w in lst:
##        if element==w:
##            c=c+1
##    if c==1:
##        uniq.append(element)
##        print('Element',element,'frequency',c)
##for q in lstc:
##    if lst.count(q)==1:
##        pass
##    else:
##        for w in range(len(lstc)-1):
##            if lstc[w]==q:
##                print('Element',q,'frequency',lstc.count(q))
##                dupl.append(q)
##                lstc.pop(w)
##print('Original List:',list(lst))
##print('Unique Elements List',uniq)
##print('Duplicates Elements List',dupl)



##Q9        
##lst=eval(input("Enter list:")) 
##length=len(lst) 
##biggest=secondbiggest=lst[0] 
##for i in range(1,length): 
##    if lst[i]>biggest :
##        secondbiggest=biggest 
##        biggest=lst[i] 
##    elif lst[i]>secondbiggest: 
##        secondbiggest = lst[i] 
##print("Largest number of the list:", biggest) 
##print("Second largest number of the list:", secondbiggest)



##Q10
##def tuplehalf():
##    tup=eval(input("Enter a tuple:")) 
##    ln=len(tup) 
##    mid=ln//2 
##    if ln%2==1: 
##        mid=mid+1 
##        half=tup[:mid] 
##    if sorted(half)==list(tup[:mid]): 
##        print("First half is sorted") 
##    else: 
##        print("First half is not sorted")
##
##tuplehalf()


##Q11
##sentence="This is a super idea This idea will change the idea of learning"
##words=sentence.split() 
##d={} 
##for one in words: 
##    key=one 
##    if key not in d: 
##        count=words.count(key) 
##        d[key]=count 
##print("Counting frequencies in list \n",words) 
##for w in d:
##    print("  "+w.ljust(15),str(d[w]).ljust(3))



##Q12
##n=int(input("How many Students?")) 
##stu={} 
##for i in range(1,n+1):
##    print()
##    print("Enter details of student",(i)) 
##    rollno=int(input("Roll number:")) 
##    name=input("Name:") 
##    marks=float(input("Marks:")) 
##    d={"Rollno" :rollno,"Name":name,"Marks": marks} 
##    key="Stu"+str(i) 
##    stu[key]=d 
##print("Students with marks > 75 are:") 
##for i in range(1,n+1): 
##    key="Stu"+str(i) 
##    if stu[key]["Marks"]>=75:
##        print("   RollNo".ljust(8),str(stu[key]["Rollno"]).ljust(3),"   Name".ljust(6),str(stu[key]["Name"]).ljust(20),"  Marks".ljust(7),str(stu[key]["Marks"]).ljust(20))
##

##Q13
##def reverse(x,y):
##    fx=open(x,"r")
##    fy=open(y,"w+")
##    k=fx.readlines()
##    for w in range(-1,-len(k)-1,-1):
##        x=k[w].rstrip("\n")
##        line=x
##        newlin=""
##        for i in range (-1,-len(line)-1,-1):
##            newlin=newlin+line[i]
##        print(newlin)
##        fy.write(newlin+"\n")
##reverse("Abc.txt","NewAbc.txt")


##Q14
##aList = [15,6,13,22,3,52,2] 
##print("Original list is:",aList) 
##for i in range(1,len(aList)): 
##    key = aList[i] 
##    j = i-1 
##    while j >= 0 and key <aList[j]: 
##        aList[j+1] = aList[j] 
##        j = j - 1 
##    else: 
##        aList[j+1] = key 
##print("List after sorting:",aList)



##Q15
##alist = [15,6,13,22,3,52,2] 
##print("original list is:",alist) 
##n=len(alist) 
##for i in range(n): 
##    for j in range(0,n-i-1): 
##        if alist[j]>alist[j+1]: 
##            alist[j],alist[j+1]=alist[j+1],alist[j] 
##print("list after sorting:",alist)



##Q16
##def encrypt(sttr,enkey): 
##    return enkey.join(sttr) 
##def decrypt(sttr,enkey): 
##    return sttr.split(enkey) 
###-main
##mainstring = input("enter main string:") 
##encryptstr = input("enter encryption key:") 
##enstr=encrypt(mainstring,encryptstr) 
##delst=decrypt(enstr,encryptstr) 
##destr="".join(delst) 
##print("the encrypted string is",enstr) 
##print("string after dcryption is:",destr)


##Q17
##def fx(file):
##    z=0
##    di={}
##    f=open(file,"r")
##    lst=f.readlines()
##    for line in lst:
##        z=z+1
##        uc=0
##        lc=0
##        for word in line:
##            if word.isupper():
##                uc=uc+1
##            elif word.islower():
##                lc=lc+1
##        di[z]=[lc,uc]
##    return di
##  
##y=fx("Abc.txt")
##print(y)


##Q18
##myfile=open("answer.txt","r") 
##line=" " 
##while line: 
##    line=myfile.readline() 
##    for word in line.split(): 
##        print(word,end='#') 
##myfile.close()




##Q19
##myfile = open("answer.txt","r") 
##ch=" " 
##vcount=0 
##ccount=0 
##while ch: 
##    ch=myfile.read(1) 
##    if ch in['a','A','e','E','i','I','o','O','u','U']: 
##        vcount=vcount+1 
##    else: 
##        ccount=ccount +1 
##print("vowels in the file:",vcount) 
##print("consonants in the file:",ccount) 
##myfile.close()


##Q20
##import pickle 
##stu={} 
##stufile=open('Stu.dat', 'wb') 
##ans='y' 
##while ans=='y' or ans=='Y':
##    rno=int(input("Enter roll number : ")) 
##    name=input("Enter name :") 
##    marks=float(input("Enter marks : ")) 
##    stu['Rollno']=rno
##    stu['Name']=name 
##    stu['Marks']=marks 
##    pickle.dump(stu, stufile) 
##    ans=input("Want to enter more records? (y/n)...") 
##stufile.close()

##Q21
##import pickle 
##stu={ }
##stufile=open('Stu.dat', 'ab') 
##ans='y' 
##while ans=='y' or ans=='Y':
##    rno=int(input("Enter roll number :")) 
##    name=input("Enter name :") 
##    marks=float( input("Enter marks: ")) 
##    stu['Rollno']=rno
##    stu['Name']=name 
##    stu['Marks']=marks
##    conf=input('Confirm(y/n):')
##    if conf=='Y' or conf=='Y':
##        pickle.dump(stu,stufile) 
##    ans = input("Want to append more records? (y/n)...") 
##stufile.close()


##Q22
##import pickle 
##stu={} 
##found=False 
##fin=open('Stu.dat', 'rb') 
##searchkeys=[46, 48] 
##try: 
##    print("Searching in File Stu.dat ...") 
##    while True :
##        stu=pickle.load(fin) 
##        if stu['Rollno'] in searchkeys:
##            print(stu) 
##            found=True 
##except EOFError: 
##    if found==False :
##        print("No such records found in the file") 
##    else: 
##        print("Search successful.") 
##    fin.close()




##Q23
##def push(s,x):
##    global top
##    s.append(x)
##    top=len(s)-1 
##def pop(s):
##    global top
##    if len(s)==0:
##        print("Underflow")
##    else:
##        x=s.pop()
##        print("poped ",x)
##        if len(s)==0:
##            top=None
##        else:
##            top=len(s)-1             
##def display(s):
##    global top
##    if len(s)==0:
##        print("stack is empty")
##    else:
##        print("Stack elements....")
##        for a in range (top,-1,-1):
##            print(s[a])   
##    
##stack=[]
##top=None
##while True:
##    print("\nStack operations")
##    print("1.Push")
##    print("2.Pop")
##    print("3.Display")
##    print("4.Exit")
##    print('top is',top)
##    ch=int(input("Enter choice : "))
##    if ch==1:
##        item=int(input("Enter data : "))
##        push(stack,item)
##    elif ch==2:
##        pop(stack)
##    elif ch==3:
##        display(stack)
##    else:
##        break


##Q24
##def fx():
##	k=[]
##	while True:
##		x=input("Enter a Line:")
##		if x=="":
##			break
##		else:
##			k.append(x)
##	print(k)
##	c=0
##	for w in k:
##		y=w.split()
##		if "cat" in y:
##			c=c+1
##	print("Count of lines containing cat",c)
##fx()

##
##Q25
##import csv 
##fh=open("Sport.csv","w") 
##writer=csv.writer(fh,delimiter='\t') 
##writer.writerow(['Sport','Competitions','Prizes won']) 
##ans='y' 
##i=1 
##while ans=='y': 
##    print("Record", i) 
##    sport=input("Sport name:") 
##    comp=int(input("No. of competitions participated :")) 
##    prizes=int(input("Prizes won:")) 
##    srec=[sport,comp,prizes] # create sequence of user data 
##    writer.writerow(srec) 
##    i=1+1 
##    ans=input("Want to enter more records? (y/n)..") 
##fh.close()



input()
