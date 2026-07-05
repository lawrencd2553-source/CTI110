# Devon Dowdy
 # Date 07/04/2026
 # P4LAB1
 # Draws a square and a triangle using turtle graphics.

import turtle

screen = turtle.Screen()
screen.bgcolor("purple")

artist = turtle.Turtle()
artist.color("lime")
artist.shape("turtle")
artist.pensize()
artist.speed(3)

side_length = 100
sides_drawn = 0

while sides_drawn < 4:
    artist.forward(side_length)
    artist.left(90)
    sides_drawn += 1

artist.left(90)
artist.forward(side_length)

artist.setheading(0)

for _ in range(3):
    artist.forward(side_length)
    artist.left(120)

screen.exitonclick()