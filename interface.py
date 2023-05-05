from turtle import Turtle
from snake import FIXED_GUI  # THE SCREEN DOESN'T SEEM TO BE CENTERED, THIS Will FIX IT

CORNER = 290


# Screen configuration
class Interface(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.color('red')
        self.penup()
        self.hideturtle()
        self.outline()

    def outline(self):
        self.goto(CORNER - FIXED_GUI, CORNER + FIXED_GUI)
        self.pendown()
        self.goto(-CORNER - FIXED_GUI, CORNER + FIXED_GUI)
        self.goto(-CORNER - FIXED_GUI, -CORNER + FIXED_GUI)
        self.goto(CORNER - FIXED_GUI, -CORNER + FIXED_GUI)
        self.goto(CORNER - FIXED_GUI, CORNER + FIXED_GUI)
        self.penup()

        # self.setup(width=600, height=600)
        # self.bgcolor("black")
        # self.title("My Snake Game")
        # self.tracer(0)
