import turtle

win = turtle.Screen()
win.screensize(1300,400)
win.bgcolor ("Navy")
t = turtle.Turtle()
t.color ("White")

def add (a,b):
    return a+b

res = add (34,56)
t.penup()
t.goto (-200,0)
t.pendown
t.write ("The sum of numbers is "+ str (res),font=('arial',24,'bold' ))

turtle.done()