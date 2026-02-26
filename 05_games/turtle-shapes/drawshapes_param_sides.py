import turtle
import random

# ----------------------------
# Screen setup
# ----------------------------
screen = turtle.Screen()
screen.colormode(255)
screen.bgcolor("white")

tim = turtle.Turtle()
tim.speed(5)
tim.pensize(2)

# ----------------------------
# Color palette (RGB)
# ----------------------------
color_list = [
    (239, 71, 111),
    (255, 209, 102),
    (6, 214, 160),
    (17, 138, 178),
    (7, 59, 76),
    (144, 190, 109),
    (249, 132, 74),
]

# ----------------------------
# Helper function
# ----------------------------
def random_color():
    return random.choice(color_list)

# ----------------------------
# Challenge 3 function
# ----------------------------
def draw_shape(num_sides):
    angle = 360 / num_sides
    tim.color(random_color())

    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

# ----------------------------
# Example usage
# ----------------------------
draw_shape(3)   # Triangle
draw_shape(4)   # Square
draw_shape(5)   # Pentagon
draw_shape(6)   # Hexagon
draw_shape(7)   # Heptagon
draw_shape(8)   # Octagon
draw_shape(9)   # Nonagon
draw_shape(10)  # Decagon

# ----------------------------
# Finish
# ----------------------------
tim.hideturtle()
screen.exitonclick()
