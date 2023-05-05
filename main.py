from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from interface import Interface
import time


DELAY = 0.1  # 0.1

# Screen configuration
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Snake configuration
ekans = Snake()
food = Food()
scoreboard = ScoreBoard()
interface = Interface()

# controls
screen.listen()
screen.onkey(key="a", fun=ekans.move_left)
screen.onkey(key="d", fun=ekans.move_right)
screen.onkey(key="s", fun=ekans.move_down)
screen.onkey(key="w", fun=ekans.move_up)

# Game on

game_over = False
while not game_over:
    screen.update()
    screen.tracer(0)  # 1 for snake no delay

    # Snake move
    ekans.move()
    time.sleep(DELAY)  # 0.01
    screen.tracer(0)

    # Detect collision with food.
    if ekans.head.distance(food) < 11:
        food.refresh_food()
        scoreboard.refresh_score()
        ekans.extend()

    # Detect Collision with walls
    if ekans.head.xcor() > 290 or ekans.head.xcor() < -290 or ekans.head.ycor() > 290 or ekans.head.ycor() < -290:
        scoreboard.collision()
        game_over = True

    # Detect Collision with the snake
    for body in ekans.segments[1:]:
        if ekans.head.distance(body) < 19:
            scoreboard.collision()
            game_over = True


screen.mainloop()
