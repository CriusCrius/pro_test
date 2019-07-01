# 案例一：
# import turtle
# # t = turtle.Turtle()
# # t.speed(1)
# # c = ['red','blue','yellow']
# # for x in range(60):
# #     t.color(c[x%3])
# #     t.fd(x*2)
# #     t.left(121)
# 案例二：
# import turtle
# t = turtle.Turtle()
# t.speed(1)
# c = ['red','blue','yellow']
# for x in range(60):
#     t.penup()
#     t.color(c[x%3])
#     t.fd(x*3)
#     t.left(121)
#     t.write('python',font=('楷体',18))
# # 案例三：
import turtle
t = turtle.Turtle()
t.speed(1)
t.color('red')
t.begin_fill()
t.circle(50, steps=4)
t.left(45)
t.fd(70)
t.circle(35,180)
t.right(90)
t.circle(35,180)
t.end_fill()
