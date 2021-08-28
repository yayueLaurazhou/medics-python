from turtle import Turtle,Screen

# Make turtle t draw a square of with side 4.
def drawSquare(t):
    for i in range(4):
        t.forward(40)
        t.left(90)

wn = Screen()  # Set up the window and its attributes
wn.bgcolor("lightgreen")

my_turtle = Turtle()  # create alex
drawSquare(my_turtle)  # Call the function to draw the square passing the actual turtle and the actual side size

wn.exitonclick()
