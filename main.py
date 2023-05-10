from turtle import *

pensize(10)
circle(50)
up()
goto(-50, -25)
down()

begin_fill()
color("red")
fd(5)
for i in range(4):
    fd(100)
    circle(27, 90)

up()
goto(-80, -25)
up()
goto(55, 95)
down()

circle(5, 360)
hideturtle()


exitonclick()
