"""
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
"""
import turtle
import random

# ----------------------------
# Screen setup
# ----------------------------
screen = turtle.Screen()
screen.title("Turtle Shapes")
screen.colormode(255)
screen.bgcolor("white")

tim = turtle.Turtle()
tim.speed(0)
tim.pensize(2)

# ----------------------------
# Color palette
# ----------------------------
color_list = [
    (239, 71, 111),
    (255, 209, 102),
    (6, 214, 160),
    (17, 138, 178),
    (7, 59, 76),
    (144, 190, 109),
    (67, 170, 139),
    (249, 132, 74),
    (248, 150, 30),
    (131, 56, 236)
]

# ----------------------------
# Helper function
# ----------------------------
def random_color():
    return random.choice(color_list)

# ----------------------------
# Draw different shapes
# ----------------------------
def draw_shape(num_sides, size):
    angle = 360 / num_sides
    tim.color(random_color())
    for _ in range(num_sides):
        tim.forward(size)
        tim.right(angle)

# ----------------------------
# Draw multiple shapes 
# ----------------------------
def draw_all_shapes():
    for sides in range(3, 11):  # triangle to decagon
        draw_shape(sides, 100)

# ----------------------------
# Spirograph 
# ----------------------------
def draw_spirograph(radius, gap):
    for _ in range(int(360 / gap)):
        tim.color(random_color())
        tim.circle(radius)
        tim.setheading(tim.heading() + gap)

# ----------------------------
# Execute drawings
# ----------------------------
tim.penup()
tim.goto(-200, 0)
tim.pendown()
draw_all_shapes()

tim.penup()
tim.goto(200, 0)
tim.pendown()
draw_spirograph(80, 10)

# ----------------------------
# Finish
# ----------------------------
tim.hideturtle()
screen.exitonclick()
