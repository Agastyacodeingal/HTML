import random
import turtle

win = turtle.Screen()
win.screensize(300,400)
win.bgcolor ("Red")
t = turtle.Turtle()

t.width(5)
t.color("Orange")


comp = random.randint(1,10)

while True:
    print("ROUND 1, FIGHT")
    n = int(input("ENTER YOUR NUMBER"))
    if (n==comp):
        t.write (("VICTORY"),font=("Times",40,'bold'))
        break
    else:
        t.write(("FATALITY"),font=("Times",40,'bold'))
    ch = input("DO YOU WISH TO CONTINUE? (YES/NO)")
    if ch.lower()=='n':
        break
turtle.done()