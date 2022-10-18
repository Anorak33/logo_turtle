from turtle import *

def whithoutDrawGoto(x, y):
    """ WhithoutDrawGoto(x, y, /)
    
        x and y : (int) """   
    penup()
    goto(x,y)
    pendown()   
   
    
def logo():
    """Make the 'aternos.org' logo in turtle interface"""
    
    # Init 
    pencolor("#2596be")
    pensize(60)
    shape("square")
    whithoutDrawGoto(-200,200)
    
    # Outside square
    for i in range(4):
        forward(400)
        right(90)
    
    whithoutDrawGoto(-110, 110)
    pensize(60)
    
    # Mid square
    for i in range(4):
        forward(60)                 
        penup()
        forward(100)
        pendown() 
        forward(60)
        right(90)
    
    
    whithoutDrawGoto(-20, 20)

    # Inside square
    
    for i in range(4):
        forward(30)
        right(90)       
        

ht()
logo()
done()
