from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_FORWARD = 20
TURN_LEFT = 180
TURN_UP = 90
TURN_RIGHT = 0
TURN_DOWN = 270

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def extend(self):
        self.add_segment(self.segments[-1].position())


    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def move(self):
        for segment_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_number - 1].xcor()
            new_y = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(new_x, new_y)
        self.head.forward(MOVE_FORWARD)


    def up(self):
        if self.head.heading() != TURN_DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != TURN_UP:
            self.head.setheading(TURN_DOWN)

    def left(self):
        if self.head.heading() != TURN_RIGHT:
            self.head.setheading(TURN_LEFT)

    def right(self):
        if self.head.heading() != TURN_LEFT:
            self.head.setheading(TURN_RIGHT)
