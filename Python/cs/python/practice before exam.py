##print(chr(57))
##print(ord("A"))


##coversion
##x=float(input("ENTER WEIGHT IN TONNES"))
##q=x*10
##kg=x*1000
##print("quintal -",q)
##print("kilogram -",kg)

##swapping
##x=int(input("ENTER NO."))
##y=int(input("ENTER 2 NO."))
##print(x,y)
##x,y=y,x
##print(x,y)
##x,y=7,2
##x,y,x=x+1,y+3,x+10
##print(x,y)
##
##
##
##
##       RANDOM CODES 
##
##
##
##from random import *
##for w in range (5):
##    print(randrange(1,10,2))
##input()
##for w in range (5):
##    print(randint(1,6))
##print()
##input()
##for w in range (5):
##    print(random())
##
##
##        CH-FLOW OF CONTROL
##s=int(input("enter"))
##if s==0 or s<=9:
##    print("its a digit")
##
##
##    for prime no.
##y=1
##x=int(input("ENTER NO."))
##for w in range(2,x):
##    d=x%w
##    if d==0:
##        y=0
##        break
##    else:
##        y=1
##if y==1:
##    print(x,"is prime")
##if y==0:
##    print(x,"is not prime")
######
######
####    stripping
####x="    ayush"
####y="ayush     "
####z="  ayush  "
####print(x.lstrip())
####print(y.rstrip())
####print(z.strip())





##a="i am pro player"
##print(a.replace("pro","noob"))
##a="*"
##print(a.join("ayush"))
##y="da#r#s#h#il"
##print(y.split("#"))
##y="i am pro player"
##print(y.partition("pro"))


'''
b="darshil"
print(b[-1::-1])
print(b[::])
print(b[::1])
print(b[0:len(b)])
print(b[::-1])

print("zdarshil"<" zayush")
a= "darshil"
print(a[2]+a[4:6])

x=int(input("Enter"))
y=int(input("Enter"))
for w in range(x,y+1):
    print(w)
'''
'''

k=[24,12,15,25,16,18]
grt=k[0]
for w in k:
    if grt<w:
        grt=w
print("grt",grt)
'''
x=input("Enter String")
k=x[::-1]
if k==x:
    print("It is Pallindrome")
else:
    print("it is not pallindrome")
