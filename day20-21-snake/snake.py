from turtle import Turtle

SIZE = 10

class Snake:
    def __init__(self):
        self.tail =[Turtle()]
        self.head = self.tail[0]
        self.head.goto(0,0)
        self.initial_snake()
        self.speed = 0

    def initial_snake(self):
        for i in range(3):
            self.add_segment()

    def add_segment(self):
        last = len(self.tail) - 1
        (new_x, new_y) = self.tail[last].pos()
        self.tail.append(Turtle())
        last = last + 1
        self.square_features(self.tail[last])
        self.tail[last].goto(new_x, new_y)

    def square_features(self, square):
        shape = SIZE * (0.05)
        square.penup()
        square.speed('slow')
        square.shape('square')
        square.color('white')
        square.shapesize(stretch_wid=shape, stretch_len=shape)

    def move(self):
        for segment in range(len(self.tail)-1, 0, -1):
            (new_x, new_y) = self.tail[segment-1].pos()
            self.tail[segment].goto(new_x, new_y)
        self.head.fd(SIZE)

    def up(self):
        if self.head.heading()==0 or self.head.heading()==180:
            self.head.setheading(90)

    def down(self):
        if self.head.heading()==0 or self.head.heading()==180:
            self.head.setheading(270)

    def right(self):
        if self.head.heading()==90 or self.head.heading()==270:
            self.head.setheading(0)

    def left(self):
        if self.head.heading()==90 or self.head.heading()==270:
            self.head.setheading(180)

    def wall_collision(self):
        if self.head.xcor() > 300 or self.head.xcor()<-300 or self.head.ycor()>300 or self.head.ycor()<-300:
            return False
        else:
            return True

    def tail_collision(self):
        for segment in self.tail[1:]:
            if self.head.distance(segment) < 0.001:
                return False

    def clear_snake(self):
        if len(self.tail)>1:
            for segment in range(len(self.tail)):
                self.tail[segment].goto(1000,1000)
