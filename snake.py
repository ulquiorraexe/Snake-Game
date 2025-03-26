from turtle import *

start = [(0, 0), (-20, 0), (-40, 0)]
distance = 20
up = 90
down = 270
right = 0
left = 180

class Snake(Turtle):

    global start
    def __init__(self):
        super().__init__()
        self.segments = []
        self.create()
        self.head = self.segments[0]
    def create(self):
        for position in start:
            self.segment(position)

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create()
        self.head = self.segments[0]

    def extend(self):
        self.segment(self.segments[-1].position())
    def segment(self, position):
        cem = Turtle(shape="square")
        cem.color("white")
        cem.penup()
        cem.goto(position)
        self.segments.append(cem)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.fd(distance)

    def up(self):
        if self.head.heading() != down:
            self.head.seth(up)

    def down(self):
        if self.head.heading() != up:
            self.head.seth(down)

    def turn_right(self):
        if self.head.heading() != left:
            self.head.seth(right)

    def turn_left(self):
        if self.head.heading() != right:
            self.head.seth(left)

