# Import turtle package
import turtle
# Creating a turtle object(vr)
vr = turtle.Turtle()
# If you wish to change the background color, you can use the bgcolor method, by default it is white.
turtle.Screen().bgcolor('black')
turtle.pensize(4) 
vr.speed (10)
# Defining a method to draw curve
def drawcurve():
    for i in range(200):
        # Defining step by step curve motion
        vr.right(1)
        vr. forward(1)
        vr.color('red', 'pink')
        #begin_fill() : When you want to fill a shape with a color, then call this method
vr.begin_fill()
#In order to change the pen's direction, use left method.
vr.left(140)
 # Draw the left line
vr.forward(111.65)
#calling the drawcurve Function
drawcurve()
vr.left(120)
drawcurve()
 # Draw the right line
vr.forward(111.65)
vr.end_fill()
vr.penup()
vr.goto(77, -40)
vr.pendown()
vr.hideturtle()

        
