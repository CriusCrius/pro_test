# 案例一:
# import turtle
# t = turtle.Turtle()
# t.speed(0)
# c = ['red','blue','pink','yellow']
# for x in range(60):
#     t.color(c[x%4])
#     t.circle(x)
#     t.left(10)

# 案例二：
import turtle
t = turtle.Turtle()
t.speed(1)
c = ['red','blue','pink','yellow']
for x in range(60):
    t.color(c[x%4])
    t.fd(x*2)
    t.left(91)