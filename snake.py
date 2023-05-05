from turtle import Turtle
# import time  # TAKE AWAY

FIXED_GUI = 4  # THE SCREEN DOESN'T SEEM TO BE CENTERED, THIS Will FIX IT
MOVE_DISTANCE = 20  # 20
# UP = 90
# DOWN = 270
# RIGHT = 0
# LEFT = 180
starting_positions = [(0-FIXED_GUI, 0 + FIXED_GUI),
                      ((-1 * MOVE_DISTANCE) - FIXED_GUI, 0 + FIXED_GUI),
                      ((-2 * MOVE_DISTANCE) - FIXED_GUI, 0 + FIXED_GUI)]


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.direction = "stop"
        self.head = self.segments[0]
        # self.head.shape("triangle")

    def create_snake(self):
        for position in starting_positions:
            self.add_segments(position)

    def add_segments(self, position):
        new_snake = Turtle()
        new_snake.penup()
        new_snake.speed("fastest")
        new_snake.shape("square")
        new_snake.color("white")
        new_snake.goto(position)
        self.segments.append(new_snake)

    def extend(self):
        self.add_segments(self.segments[-1].position())

    def move(self):
        x = self.head.xcor()
        y = self.head.ycor()

        if self.direction != "stop":
            for seg_num in range(len(self.segments) - 1, 0, -1):
                new_segment = self.segments[seg_num-1].position()
                self.segments[seg_num].goto(new_segment)
            # self.head.forward(MOVE_DISTANCE)  # old version

        # new version
        if self.direction == "up":
            y += MOVE_DISTANCE
        elif self.direction == "down":
            y -= MOVE_DISTANCE
        elif self.direction == "left":
            x -= MOVE_DISTANCE
        elif self.direction == "right":
            x += MOVE_DISTANCE

        self.head.goto(x, y)

    def move_up(self):
        if self.direction != "down":
            self.direction = "up"
            # self.head.setheading(UP)  # old version

    def move_down(self):
        if self.direction != "up":
            self.direction = "down"
            # self.head.setheading(DOWN)  # old version

    def move_right(self):
        if self.direction != "left":
            self.direction = "right"
            # self.head.setheading(RIGHT)  # old version

    def move_left(self):
        if self.direction != "right":
            self.direction = "left"
            # self.head.setheading(LEFT)  # old version
