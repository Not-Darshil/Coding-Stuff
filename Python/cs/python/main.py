##for a in range(6):
##    print(a,end="*")
##print()
##for b in range(2,6):
##    print(b,end="*")
##print()
##for b in range(12,6,-1):
##    print(b,end="*")
##print()
##for b in range(2,9,2):
##    print(b,end="*")
##print()
##for b in range(2,9,3):
##    print(b,end="*")
##print()
##for b in range(10,40,5):
##    print(b,end="*")
##print()
##for b in range(3,31,3):
##    print(b,end="*")
##print()
##for b in range(1,11):
##    print(b,end="*")
##print()
##for b in range(1,11):
##    print(b*8,end="*")
##print()
##for b in range(1,11,-1): #no output
##    print(b,end="*")
##print()
##for b in range(4,20,7):
##    print("#",b,end="*")
##    print("zzz")
##for b in range(20,2,-2):
##    print(b,end="*")
##    
##print()
##for b in "aman":
##    print(b,end="*")
##print()
##for b in "vanasthali":
##    print(b,end=" ravi ")
##print()
##print("ravi\n"*10)
##
##print()
##for w in "31657":
##    print(int(w)+1,end="*")
##
##print()
##for w in "45":
##    print(int(w)+1,end="*")
##    
#slice
##alt+3 to make selection as comment
##and alt + 4 to remove the comment
##print()
##a="sundar"
####012345
####-6-5-4-3-2-1
###"012345"
##print(a[0],a[5],a[-2])
##v=4397
##print(v[0]) #error
##0 is index or subscript
##v=4397
##w=str(v)
##print(w[0],w[3],sep='') 
##print(w[3])
##print(v%10)
##print(w[-1])
##print(int(w[3])*2)
##print(int(w[-1])*2)
##print(v%10*2)
#read a number from the user
#and display  the sum of its digits

##n=input("Enter a number : ")
##sum=0
##for w in n:
##    print("w is ",w)
##    sum=sum+int(w)
##print(sum)
##
####read a number from the user and
####dispaly it in reverse
##412
##214

##x=input("Enter a number : ") #417
##rev=''  #"" 4   14   714
##for w in x:
##    print()
##    print(x,w,rev)
##    rev=w+rev
##    #rev=4+"" means rev=4
##    ##now w is 1
##    #rev='1'+'4' means rev=14
##    #now w is 7
##    #rev='7'+'14' means rev=714
##    print("Now rev is ",rev)
##print(rev)

##x=input("Enter a number : ") #417
##rev=''  #"" 4   14   714
##for w in x:
##    rev=w+rev
##print(rev)

#read a number and display its table
##x=int(input("Enter a number : "))
##for w in range(1,11):
##    print(w*x)

#Read a number and display its table in
#reverse order.
##x=int(input("Enter a number : "))
##for w in range(10,0,-1):
##    print(w*x)

##if statement
##
##if 2<5:
##    print("hello")
##else:
##    print("hi")
##    
##if 12<5:
##    print("hello")
##else:
##    print("hi")
##a=33
##if a==33:
##    print("x")
##else:
##    print("y")
##    
##if 35%2==0:
##    print("Even")
##else:
##    print("Odd")
##    
##if 350%2==0:
##    print("Even")
##else:
##    print("Odd")
##    
#Read 5 numbers and display thir sum
##sum=0
##for w in range(5):
##    x=int(input("Enter a number "))
##    sum=sum+x
##    print("sum is ",sum)
##print(sum)
    
#Read 5 numbers and display sum of even nos
##sum=0
##for w in range(5):
##    x=int(input("Enter a number "))
##    if x%2==0:
##        sum=sum+x
##    print("sum is ",sum)
##print(sum)

#Read 5 numbers and count even nos
##z=0
##for w in range(5):
##    x=int(input("Enter a number "))
##    if x%2==0:
##        z=z+1
####    print("even count is ",z)
##print(z)

#read 6 numbers and display the count
#of odd numbers
##z=0
##for w in range(6):
##    x=int(input("Enter a number "))
##    if x%2!=0:
##        z=z+1
####    print("odd count is ",z)
##print(z)

##read 4 numbers and display the numbers which are fully
##divisible by 7

#read 10 integers from the user and display the 
##sum of last digit of all of the numbers
##z=0
##for w in range(10):
##    x=int(input("Enter a number "))
##    z=z+x%10
##print("The sum is",z)
    


#read an integers from the user and display the 
##sum of its digits
##eg no is 412 ans 7
##sum=0
##x=input("Enter a number ") #'491'
##for w in x:  #w 4 9 1 
##    sum=sum+int(w) #type casting
##print("The sum is",sum)

#read an integers from the user and display the 
##sum of its even digits
##eg no is 412 ans 6

##sum=0
##x=input("Enter a number ") #'491'
##for w in x:  #w 4 9 1
##    if int(w)%2==0:
##        sum=sum+int(w) #type casting
##print("The sum is",sum)

#read an integers from the user and display the 
##sum of its odd digits
##eg no is 4125 ans 6

##sum=0
##x=input("Enter a number ") #'491'
##for w in x:  #w 4 9 1
##    if int(w)%2==1:
##        sum=sum+int(w) #type casting
##print("The sum is",sum)

#Read 5 numbers and display that how many of
##them are -ive
# eg
# 5 -3 6 7 -88
##result 2

##cnt=0
##for w in range (5):
##    n=int(input("Enter  a number " ))
##    if n<0:
##        cnt=cnt+1
##print("-ive numbers ",cnt)

#Read 5 numbers and display that how many of
##them are fully divisble by 7
# eg
# 14 -3 6 7 -88
##result 2

#Read 7 numbers and display the sum of
##the numbers fully divisble by 3


#read a number and display the sum of its
#even digits
#234
#output
#6
##
##sum=0
##x=input("Enter a number ") 
##for w in x:
##    if int(w)%2==0:
##     sum=sum+int(w) 
##print("The sum is",sum)

##read 2 numbers and display the
##number whose sum of digits is greater
##eg 99 11223
##18 9
##output 99

##s1=s2=0
##x=input("Enter a number ")
##y=input("Enter a number ")
##for w in x:
##    s1=s1+int(w)
##for w in y:
##    s2=s2+int(w)
##if s1>s2:
##    print(x)
##else:
##    print(y)
##    

##
##if 15<=5:
##    print(9)
##    print(6)
##    print('hello')
##else:
##    print(2)
##    print('school')
##print('zzz')
##
##print(4<=5)
##print(5<=5)
##print(14<5)
##print(int(4<=5))
##print(int(5<=5))
##print(int(14<5))
##print(bool(1))
##print(bool(0))
##print()
##print(bool(4))
##print(bool(5524))


#anything besides 0 (zero) is True
#only 0 is False
##T and F for True and False is Capital
##rest small

print()
print(bool(-71))
print(bool(0))


##True/False are the vaues of boolean
#int value for True is 1
#int value of False is 0

#read 2 numbers and display square of
#smaller number

#read a number and display cube of its
##second last digit
#527
#8

##x=input("Ente a number ")
##print(int(x[-2])**3)

##read a 2 digit number and display
##sum of square of all of its digits
#23 input
#13 output

x=input("Enter a 2 digit number : ")
##f=int(x[0])**2
##s=int(x[1])**2
##sum=f+s
##print("Sum of square of digits is ",sum)
print("sum is ",int(x[0])*2+int(x[1])*2)
