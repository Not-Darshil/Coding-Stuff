import turtle
t=turtle.Turtle()
wn=turtle.Screen()
t.speed(6)
t.hideturtle()
wn.bgcolor("light blue")
t.color("yellow")
t.up()
t.goto(-385,-200)
t.down()
t.left(60)
k=[2.15,2.5,3]
t.begin_fill()
t.fillcolor("Brown")
t.color("Brown")
for w in k:
    t.fd(w*100)
    t.right(120)
    t.fd(w*100)
    t.left(120)
t.goto(385,-385)
t.goto(-385,-385)
t.end_fill()
t.up()
t.goto(250,250)
t.down()
t.begin_fill()
t.color("yellow")
t.fillcolor("yellow")
t.circle(75)
t.end_fill()
t.up()
t.goto(50,-150)
t.down()
t.goto(100,-385)
t.begin_fill()
t.color("blue")
t.fillcolor("blue")
t.goto(150,-385)
t.goto(100,-200)
t.goto(50,-150)
t.end_fill()
t.up()
        

    
    
    
    


