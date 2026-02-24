from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        # random_x = random.randint(-280, 280)
        # random_y = random.randint(-280, 280)
        FOOD_LIMIT = 270  # buffer so food never touches the wall
        random_x = random.randint(-FOOD_LIMIT, FOOD_LIMIT)
        random_y = random.randint(-FOOD_LIMIT, FOOD_LIMIT)
        self.goto(random_x, random_y)
