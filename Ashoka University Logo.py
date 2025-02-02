import turtle
import math

t = turtle.Turtle()
t.speed(0)
t.color("#D71920")
t.penup()
t.goto(0, -50)
t.pendown()

for i in range(10):
    angle = i * 36
    x = 50 * math.sin(math.radians(angle))
    y = 50 * math.cos(math.radians(angle))
    t.penup()
    t.goto(x, y - 100)
    t.pendown()
    t.circle(100)

t.penup()
t.goto(0,-149)
t.pendown()
t.width(2)
t.circle(149)

t.penup()
t.goto(0,-135)
t.pendown()
t.width(1)
t.circle(135)

t.penup()
t.goto(0,-120)
t.pendown()
t.circle(120)

t.penup()
t.goto(0,-103)
t.pendown()
t.circle(103)

t.penup()
t.goto(0,-87)
t.pendown()
t.circle(87)

t.penup()
t.goto(0,-72)
t.pendown()
t.circle(72)

t.penup()
t.goto(0,-62)
t.pendown()
t.circle(62)

t.penup()
t.goto(0,-51)
t.pendown()
t.color("#FFFFFF")
t.width(6.4)
t.circle(51)

t.fillcolor()

t.hideturtle()
turtle.done()
