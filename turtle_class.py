from turtle import Turtle,Screen
my_turtle = Turtle()
#print(t)

my_screen = Screen()
my_screen.bgcolor("lightgreen")

for i in range(4):
    my_turtle.forward(40)
    my_turtle.left(90)

my_screen.exitonclick()