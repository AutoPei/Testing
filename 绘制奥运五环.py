import turtle

r = 50  #设置五环半径
g = 15   #设置五环间隔
p = 8   #设置画笔粗细
g1 = 50 #五环与方框之间的间隔

turtle.pensize(p) #初始化画笔粗细

#以黑色圆环作为坐标（0,0）
#第一层，黑色，绘画起始位置坐标（r,0)
turtle.penup()
turtle.goto(0,-1*r)
turtle.pendown()
turtle.color('black')
turtle.circle(r)

#第一层，蓝色
turtle.penup()
turtle.goto(-1*(2*r+g),-1*r)
turtle.pendown()
turtle.color('blue')
turtle.circle(r)

#第一层，红色
turtle.penup()
turtle.goto(2*r+g,-1*r)
turtle.pendown()
turtle.color('red')
turtle.circle(r)

#第二层，橙色
turtle.penup()
turtle.goto(-1*(r+g/2),-2*r)
turtle.pendown()
turtle.color('orange')
turtle.circle(r)

#第二层，绿色
turtle.penup()
turtle.goto(r+g/2,-2*r)
turtle.pendown()
turtle.color('green')
turtle.circle(r)

#增加方框，离圆环的距离为g1
turtle.penup()
turtle.goto(-1*(3*r+g+g1),r+g1)
turtle.pendown()
turtle.color('brown')
turtle.goto(3*r+g+g1,r+g1)
turtle.goto(3*r+g+g1,-1*(2*r+g1))
turtle.goto(-1*(3*r+g+g1),-1*(2*r+g1))
turtle.goto(-1*(3*r+g+g1),r+g1)

#结束绘画
turtle.done()