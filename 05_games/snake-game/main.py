from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
# need to add following when running from IDEs like Pycharm
#screen.focus_force()
screen.onkey(lambda: print("UP pressed"), "Up")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    print(snake.head.xcor(), snake.head.ycor())

    #Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall.
    # if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
    WALL_LIMIT = 290  # 300 (half screen) - 10 (half snake size)

    # Detect collision with wall
    if (
            snake.head.xcor() > WALL_LIMIT or
            snake.head.xcor() < -WALL_LIMIT or
            snake.head.ycor() > WALL_LIMIT or
            snake.head.ycor() < -WALL_LIMIT
    ):
        game_is_on = False
        scoreboard.game_over()


    #Detect collision with tail.
    # for segment in snake.segments[1:]:
    #     if snake.head.distance(segment) < 10:
    #         game_is_on = False
    #         scoreboard.game_over()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
