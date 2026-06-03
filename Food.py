from turtle import Turtle
import random

class Food(Turtle):

    ### Create the food object as a small red circle ###

    def __init__(self):

        super().__init__()
        self.shape("circle")
        self.color("Red")
        self.penup()
        self.shapesize(0.5, 0.5)   ### Make the food smaller than default###
        self.speed("fastest")

    ### Move food to a random position on the screen ###

    def refresh(self):

        x_pos = random.randint(-280, 280)
        y_pos = random.randint(-280, 280)
        self.goto(x_pos, y_pos)


