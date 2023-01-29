import turtle

t = turtle.Pen()
turtle.bgcolor("black")

for x in range(360):

    if x % 6 == 0:
        t.pencolor('red')
    elif x % 6 == 1:
        t.pencolor("purple")
    elif x % 6 == 2:
        t.pencolor("orange")
    elif x % 6 == 3:
        t.pencolor("blue")
    elif x % 6 == 4:
        t.pencolor("green")
    elif x % 6 == 5:
        t.pencolor("yellow")

    t.width(x // 100 + 1)
    t.forward(x)
    t.left(59)

turtle.exitonclick()
