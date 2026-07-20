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

    

    def create_snake(self):

        ''' Create the snake with 3 segment at start ''' 

        for position in STARTING_POSITION:
            self.add_segment(position)

    

    def add_segment(self, position):

        ''' Add one new segment to the snake '''

        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    

    def reset(self):

        ''' Reset the snake for a new game '''

        for seg in self.segments:
            seg.goto(1000, 1000)   ### Move old segments far away ###
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    

    def extend(self):

        ''' Make the snake longer when it eats food '''

        self.add_segment(self.segments[-1].position())

    

    def move(self):

        ''' Move the snake forward ''' 

        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    

    def up(self):

        ''' Change direction to up (cannot go back down) '''

        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    

    def down(self):

        ''' Change direction to down (cannot go back up) '''

        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    

    def left(self):

        ''' Change direction to left (cannot go back right) '''

        if self.head.heading() != RIGHT:
            
            self.head.setheading(LEFT)

    

    def right(self):

        ''' Change direction to right (cannot go back left) '''

        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)



