print("Name".ljust(30),"Class".ljust(20),"Roll no.".ljust(25),sep="")
s = "VPS STUDENTS"
# Printing the original string
print ("The original string is :", s)
# Printing the center aligned string 
print ("The center aligned string is : ")
print (s.center(30), "\n")
# Printing the center aligned 
# string with fillchr
print ("Center aligned string with fillchr: ")
print (s.center(30, '#'))
print (s.ljust(30, '*'))
print (s.rjust(30, '3'))
print ('vps'.center(6, '3'))
'''
The original string is : VPS STUDENTS
The center aligned string is : 
         VPS STUDENTS          

Center aligned string with fillchr: 
#########VPS STUDENTS#########
VPS STUDENTS********
333333333333333333VPS STUDENTS
3vps33
'''
