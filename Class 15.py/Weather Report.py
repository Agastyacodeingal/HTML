import turtle

win = turtle.Screen()
win.screensize(1300,400)
win.bgcolor ("Light Green")
t = turtle.Turtle()
t.color ("White")

def weather():
    
    spring = "The flowers will bloom in Spring  "
    Autmn = "The leaves shed in Autmn"
    
    t.penup()
    t.goto(-200,0)
    t.pendown()
    t.write(spring+Autmn,font=('arial',14,'bold'))
    
    
weather()

turtle.done()