from turtle import Screen
from Food import Food
from Snake import Snake
from ScoreBoard import ScoreBoard
import time
from types import new_class

screen = Screen()
screen.bgcolor("black")
screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up , "w")
screen.onkey(snake.down , "s")
screen.onkey(snake.left , "a")
screen.onkey(snake.right , "d")

game_is_on = True
food.refresh()
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:

        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:

        scoreboard.reset()
        snake.reset()


    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:

            scoreboard.reset()
            snake.reset()



















