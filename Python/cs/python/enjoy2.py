import turtle
import random as rm
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("black")
t.ht()
l=["red","orange","green","magenta","yellow","purple","cyan","white","blue"]
def moon(pos):
    x,y=pos
    t.pu()
    t.goto(pos)
    t.pd()
    t.fillcolor("white")
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    t.fillcolor("black")
    t.begin_fill()
    t.pu()
    t.goto(x+14,y+16)
    t.pd()
    t.circle(50)
    t.end_fill()
    
def star(pos,color,leng):
    t.up()
    t.goto(pos)
    t.pd()
    for i in range(5):
        t.speed(0)
        t.fillcolor(color)
        t.begin_fill()
        t.fd(leng)
        t.rt(144)
        t.fd(20)
        t.end_fill()
def text(color):
    t.color(color)
    t.pu()
    t.goto(-270,-600)
    t.pd()
    t.write("GOOD NIGHT",font=("algerian",24),move=True)

t.speed(0)
moon((-250,600))   
while True:
    pos=(rm.randint(-350,400),rm.randint(-600,600))
    color=rm.choice(l)     
    star(pos,color,23) 
            
    text(color)

#    t.pu()
#    t.goto(-i-66,i*3)
#    t.pd()
# 
#    t.goto(-i+75,-i*6)

   
turtle.done()
