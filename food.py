from turtle import Turtle
import random
from snake import FIXED_GUI  # THE SCREEN DOESN'T SEEM TO BE CENTERED, THIS Will FIX IT


# Food configuration
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=(2/4), stretch_wid=(2/4))
        self.color("blue")
        self.speed("fastest")
        self.refresh_food()

    def refresh_food(self):
        random_x = random.randint(-14, 14) * 20
        random_y = random.randint(-14, 14) * 20
        self.goto(random_x - FIXED_GUI, random_y + FIXED_GUI)
