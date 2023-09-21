import turtle

t = turtle.Turtle()
s = turtle.Screen()

# Set background color and pen color
s.bgcolor('#262626')
t.pencolor('magenta')
t.speed(100)

# Define a list of colors
col = ('cyan', 'yellow', 'red', 'light green')

# Outer loop for creating 5 shapes
for n in range(5):
    # Inner loop for drawing each shape
    for x in range(8):
        t.speed(x + 10)  # Adjust the drawing speed
        for i in range(2):
            t.pensize(2)  # Set pen size
            t.circle(80 + n * 20, 90)  # Draw a quarter circle
            t.lt(90)  # Turn left 90 degrees
        t.lt(45)  # Turn left 45 degrees after completing the shape
    t.pencolor(col[n % 4])  # Change pen color for the next shape

# Exit when the user clicks the screen
s.exitonclick()
turtle.done()