from turtle import *
from random import randint

track = Turtle ()
track.penup()
track.hideturtle()
track.speed()

track.goto(0, -260)
track.pendown()
track.color("black", "#fcacb1")
track.begin_fill()
track.circle(270)
track.end_fill()

track.penup()
track.goto(0, -100)
track.pendown()
track.color("black", "green")
track.begin_fill()
track.circle(110)
track.end_fill()

t1 = Turtle()
t1.color("red")
t1.shape("turtle")
t1.penup()
t1.goto(0, -120)
t1.pendown()

t2 = Turtle()
t2.color("orange")
t2.shape("turtle")
t2.penup()
t2.goto(0, -160)
t2.pendown()

t3 = Turtle()
t3.color("blue")
t3.shape("turtle")
t3.penup()
t3.goto(0, -200)
t3.pendown()

t4 = Turtle()
t4.color("yellow")
t4.shape("turtle")
t4.penup()
t4.goto(0, -240)
t4.pendown()

for i in range(118):
  t1.circle(130, randint(1,5))
  t2.circle(170, randint(1,5))
  t3.circle(210, randint(1,5))
  t4.circle(250, randint(1,5))