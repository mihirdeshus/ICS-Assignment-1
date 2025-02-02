import turtle

def koch_curve(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        length = length / 3
        koch_curve(t, length, depth - 1)
        t.left(60)
        koch_curve(t, length, depth - 1)
        t.right(120)
        koch_curve(t, length, depth - 1)
        t.left(60)
        koch_curve(t, length, depth - 1)

def koch_snowflake():
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-150, 100)
    t.pendown()
    depth = 3
    length = 300
    
    for _ in range(3):
        koch_curve(t, length, depth)
        t.right(120)  
        
    t.hideturtle()
    turtle.done()

koch_snowflake()


