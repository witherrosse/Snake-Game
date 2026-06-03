from turtle import Screen
from Food import Food
from Snake import Snake
from ScoreBoard import ScoreBoard
import time

## Setup the game window ###


screen = Screen()
screen.bgcolor("black")
screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.tracer(0)   # Turn off animation for manual control

### Create game objects ###

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

### Keyboard controls ###

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_is_on = True
food.refresh()

###  Main game loop ###
while game_is_on:
    screen.update()      ### Refresh the screen ###

    time.sleep(0.1)      ### Control game speed ###
    snake.move()

    ### Check if snake eats food ###

    if snake.head.distance(food) < 15:

        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    ### Check if snake hits the wall ###

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:

        scoreboard.reset()
        snake.reset()

    ### Check if snake hits its own body ###
    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()