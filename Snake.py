from turtle import Turtle

STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):

        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    ###  Create the snake with 3 segments at start ###

    def create_snake(self):

        for position in STARTING_POSITION:
            self.add_segment(position)

    ###  Add one new segment to the snake ###

    def add_segment(self, position):

        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    ### Reset the snake for a new game ##

    def reset(self):

        for seg in self.segments:
            seg.goto(1000, 1000)   ### Move old segments far away ###
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    ### Make the snake longer when it eats food ##3

    def extend(self):

        self.add_segment(self.segments[-1].position())

    ### Move the snake forward ###

    def move(self):

        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    ### Change direction to up (cannot go back down) ###

    def up(self):

        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    ### Change direction to down (cannot go back up) ###

    def down(self):

        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    ### Change direction to left (cannot go back right) ###

    def left(self):

        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    ### Change direction to right (cannot go back left) ###

    def right(self):

        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)



