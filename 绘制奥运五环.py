import turtle

r = 50  #设置五环半径
g = 15   #设置五环间隔
p = 8   #设置画笔粗细

turtle.pensize(p) #初始化画笔粗细

#以黑色圆环作为坐标（0,0）
#第一层，黑色
turtle.penup()
turtle.goto(r,0)
turtle.pendown()
turtle.color('black')
turtle.circle(r)

#第一层，蓝色
turtle.penup()
turtle.goto(-1*(r+g),0)
turtle.pendown()
turtle.color('blue')
turtle.circle(r)

#第一层，红色
turtle.penup()
turtle.goto(3*r+g,0)
turtle.pendown()
turtle.color('red')
turtle.circle(r)

#第二层，橙色
turtle.penup()
turtle.goto(-1*g/2,-1*r)
turtle.pendown()
turtle.color('orange')
turtle.circle(r)

#第二层，绿色
turtle.penup()
turtle.goto(2*r+g/2,-1*r)
turtle.pendown()
turtle.color('green')
turtle.circle(r)

#结束绘画
turtle.done()