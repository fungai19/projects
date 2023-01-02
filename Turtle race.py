# Fungai Jani, Mumu Kuzanga Turtle Race CS10000-01

import turtle
import random

from turtle import *
import time

# SCREEN SETUP
setup(800, 500)
title("Turtle Race")
bgcolor("forestgreen")
speed(0)
 


# FINISH LINE
gap_size= 20
shape("square")
penup()

color("white")
for i in range(10):
    goto(250, (170 - (i * gap_size * 2)))
    stamp()
    
    
for i in range(10):
    goto(250 + gap_size, ((210 - gap_size) - (i * gap_size * 2)))
    stamp()
    
color("black")
for i in range(10):
    goto(250, (190 - (i * gap_size * 2)))
    stamp()
    
for i in range(10):
    goto(251 + gap_size, ((190 - gap_size) - (i * gap_size * 2)))
    stamp()
 
#CREATING THE TURTLES
Fez = Turtle()
Fez.color('blue')
Fez.shape('turtle')
Fez.penup()
Fez.goto(-300, 150)
Fez.pendown()

 

mrm= Turtle()
mrm.color('red')
mrm.shape('turtle')
mrm.penup()
mrm.goto(-300, 100)
mrm.pendown()

 

mags= Turtle()
mags.color('black')
mags.shape('turtle')
mags.penup()
mags.goto(-300, 50)
mags.pendown()

 

maggie=Turtle()
maggie.color('yellow')
maggie.shape('turtle')
maggie.penup()
maggie.goto(-300, 0)
maggie.pendown()

 

trent= Turtle()
trent.color('purple')
trent.shape('turtle')
trent.penup()
trent.goto(-300, -50)
trent.pendown()
 
# RACE
from random import randint
while Fez.xcor() <=230 and mrm.xcor() <=230 and mags.xcor() <=230 and maggie.xcor() <=230 and trent.xcor() <=230:
    Fez.forward(randint(1,5))
    mrm.forward(randint(1,5))
    mags.forward(randint(1,5))
    maggie.forward(randint(1,5))
    trent.forward(randint(1,5))
    
# PRINT THE WINNER
if Fez.xcor()> mrm.xcor() and Fez.xcor()> mags.xcor() and Fez.xcor()>maggie.xcor() and Fez.xcor()>trent.xcor():
    print("Fez wins!")
    for i in range(72):
        Fez.right(5)
    
elif mrm.xcor()>Fez.xcor() and mrm.xcor()>mags.xcor() and mrm.xcor()>maggie.xcor() and mrm.xcor()>trent.xcor():
    print("MRM wins!")
    for i in range(72):
        mrm.right(5)
    
elif mags.xcor()>Fez.xcor() and mags.xcor()>mrm.xcor() and mags.xcor()>maggie.xcor() and mags.xcor()>trent.xcor():
    print("Mags wins!")
    for i in range(72):
        mags.right(5)
        
elif maggie.xcor()>Fez.xcor() and maggie.xcor()>mrm.xcor() and maggie.xcor()>mags.xcor() and maggie.xcor() >trent.xcor():
    print("Maggie wins!")
    for i in range(72):
        maggie.right(5)
else:
    print("Trent wins!")
    for i in range(72):
        trent.right(5)
    