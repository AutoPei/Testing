import math
import turtle

x1, y1 = 100, 100
x2, y2 = 100, -100
x3, y3 = -100, -100
x4, y4 = -100, 100

turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
turtle.goto(x2,y2)
turtle.goto(x3,y3)
turtle.goto(x4,y4)

distance = math.sqrt((x1-x2)**2+(y1-y2)**2)
turtle.color('red')
turtle.write("x1,x2与y1,y2的距离:"+str(distance),font=("Arial", 10, "normal","bold"))

turtle.done()