import turtle

win = turtle.Screen()
win.screensize(1300,400)
win.bgcolor ("Forest Green")
t = turtle.Turtle()

t.width(5)
t.color("White")
n = 4
a = 360/n
for i in range (n):
    t.forward (100)
    t.right(a)
    
    
    
    
turtle.done()