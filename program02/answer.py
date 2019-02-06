#Name goes here
import turtle

tess = turtle.Turtle()
tess.color("blue")
tess.shape("turtle")
w = turtle.Screen()
for i in range(8):
    tess.forward(100)
    tess.left(45)

w.exitonclick()
