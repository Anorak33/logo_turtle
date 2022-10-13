from turtle import *
from time import *

def logo():
    pencolor("#2596be")
    penup()
    goto(-200,200)
    pendown()
    pensize(80)
    for i in range(4):
        forward(400)
        right(90)


logo()
