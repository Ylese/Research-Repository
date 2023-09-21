from turtle import Turtle, Screen

shapes = Turtle()
sideNums = 5

def drawShapes():
    # Triangle, Square, Pentagon, Hexagon, Heptagon, Octagon/octagon
    angle = 360 / sideNums
    for _ in range(sideNums):
        shapes.forward(100)
        shapes.left(angle)

    return

shapesScreen = Screen()
drawShapes()  # Call the drawShapes function to draw the shapes
shapesScreen.exitonclick()
