from turtle import *

def whithoutDrawGoto(x, y):
    """ WhithoutDrawGoto(x, y, /)
    
        x and y : (int) """   
    penup()
    goto(x,y)
    pendown()
    
def logo():
    """Make the 'github.com' logo in turtle interface"""

    # Init
    speed(5)
    whithoutDrawGoto(0,-200)
    
    # Back Circle
    color("white", "black")
    begin_fill()
    circle(200)
    end_fill()   
    
    #Shape 
    color("white", "white")
    begin_fill()
    whithoutDrawGoto(-50,-190)


logo()
done()