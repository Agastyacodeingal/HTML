import turtle

win = turtle.Screen()
win.screensize(1300,400)
win.bgcolor ("Light Green")
t = turtle.Turtle()

t.width(5)
t.color ("White")
size = 5
while True:
    t.forward(size)
    t.right (90)
    size = size+3