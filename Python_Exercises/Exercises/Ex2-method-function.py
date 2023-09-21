#  This line imports the Turtle class and the Screen class from the Turtle graphics library.
from turtle import Turtle, Screen

#  This line creates a Turtle object named drawing.
drawing = Turtle()

# This sets the shape of the turtle cursor to "circle," so it appears as a black circular cursor.
drawing.shape("circle")

# This sets the color of the drawing turtle to black.
drawing.color("black")

#  This line sets the pen size (line thickness) to 3.
drawing.pensize(width=3)

# This defines a function called drawSquare that will draw a square.
def drawSquare():
    drawing.forward(100) # This moves the turtle forward by 100 units.
    drawing.left(90) # This turns the turtle 90 degrees to the left, creating a corner of the square.
    drawing.forward(100)
    drawing.left(90)
    drawing.forward(100)
    drawing.left(90)
    drawing.forward(100)
    drawing.left(90)


drawSquare() # Draws a square with a black outline.
drawing.color("magenta") # Changes the turtle's color to magenta.
drawSquare() # Draws a square with a magenta outline.
drawing.color("cyan") #  Changes the turtle's color to cyan.
drawSquare() # Draws a square with a cyan outline.
drawing.color("wheat") # Changes the turtle's color to wheat.
drawSquare() # Draws a square with a wheat outline.
drawing.color("yellow") # Changes the turtle's color to yellow.
drawSquare() # Draws a square with a yellow outline.

screen = Screen() # This creates a Screen object named screen.
screen.title("Drawing some square") # This sets the title of the graphics window to "Drawing some squares."
screen.exitonclick() # This makes the program wait for a user click on the screen to close the graphics window.