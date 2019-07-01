# 案例1：
# import turtle
#
#
# t = turtle.Turtle()
# t.speed(0)
# t.color('red')
# t.begin_fill()
# t.circle(90)
# t.end_fill()
# t.color('blue')
# t.begin_fill()
# t.circle(80)
# t.end_fill()
# t.color('pink')
# t.begin_fill()
# t.circle(70)
# t.end_fill()
# t.color('yellow')
# t.begin_fill()
# t.circle(60)
# t.end_fill()


#  案例2：
import turtle
t = turtle.Turtle()
t.speed(1)
t.penup()
t.goto(80, 70)  # 开始画右眼
t.pendown()
t.begin_fill()
t.circle(18)
t.end_fill()

t.penup()
t.goto(-80, 70)  # 左眼
t.pendown()
t.begin_fill()
t.circle(18)
t.end_fill()

t.penup()
t.goto(0, -110)  # 画脸
t.pendown()
t.circle(150)

t.color('red')  # 鼻子
t.penup()
t.goto(0, 60)
t.pendown()
t.begin_fill()
t.circle(-50, steps=3)
t.end_fill()

t.color('black')  # 嘴巴
t.penup()
t.goto(-80, -60)
t.pendown()
t.goto(0, -110)
t.goto(80, -60)