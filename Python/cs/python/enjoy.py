import turtle
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("#ADD8E6")
#t.up()
#t.goto(-300,20)
#t.write("vivek",font=("algeria",44))
#t.home()
#t.down()
l=["red","blue","orange","cyan","purple"]
for i in range(0,200):
    t.color(l[i%5])
    t.pensize(i/11)
    #t.circle(i+8,steps=5)
    t.speed(100)
    t.ht()
    t.fd(i)
    t.left(40)#81,90,160,190,260 star,290,10
    t.bk(i)
    t.left(900)#5
   #(30,5)
while True:
    pass
