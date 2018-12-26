import turtle
import time

turtle.speed('slowest')
turtle.pensize(2)
turtle.bgcolor("black")
colors = ['red','yellow','purple','blue']
#turtle.tracer(False)

for x in range(250):
    turtle.forward(2*x)
    turtle.color(colors[x%4])
    turtle.left(91)
time.sleep(3)
#turtle.tracer(True)