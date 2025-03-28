import turtle

win = turtle.Screen()
win.screensize(1300,400)
win.bgcolor ("Black")
t = turtle.Turtle()

t.width(5)
t.color ("White")
size = 5
while True:
    t.forward(size)
    t.right (90)
    size = size+3
    
turtle.color(1,1,1)