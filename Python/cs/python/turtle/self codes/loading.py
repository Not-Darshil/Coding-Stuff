a=0
import turtle
t=turtle.Turtle()
wn=turtle.Screen()
wn.bgcolor("orange")
t.color("black")
t.up()
t.goto(0,-50)
t.speed(6)
t.down()
while a<5:
    t.up()
    t.goto(0,-50)
    t.down()
    t.circle(50)
    t.up()
    t.goto(0,-60)
    t.down()
    t.begin_fill()
    t.circle(60)
    t.fillcolor("black")
    t.end_fill
    a=a+1
    
    
