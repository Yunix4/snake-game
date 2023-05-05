from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 20, 'normal')


# Scoreboard configuration
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.score = -1
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def collision(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        self.goto(0, -250)
        self.write("""
⣿⣷⡶⠚⠉⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠠⣴⣿⣿⣿⣿⣿⣿⣿
⠿⠥⢶⡏⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⢀⣴⣷⣌⢿⣿⣿⣿⣿⣿⣿
⣍⡛⢷⣠⣿⣿⣿⣿⣿⣟⠻⣯⠽⣿⣿⠟⠁⣠⠿⠿⣿⣿⣎⠻⣿⣿⣿⡿⠟
⣿⣿⣦⠙⣿⣿⣿⣿⣿⣿⣷⣏⡧⠙⠁⣀⢾⣧ ⠈⣿⡟ ⠙⣫⣵⣶⠇⣋⣿⣿
⣿⣿⣿⢀⣿⣿⣿⣿⣿⣿⣿⠟⠃⢀⣀⢻⣎⢻⣷⣤⣴⠟ ⣠⣾⣿⢟⣵⡆⢿
⣿⣯⣄⢘⢻⣿⣿⣿⣿⡟⠁⢀⣤⡙⢿⣴⣿⣷⡉⠉⢀ ⣴⣿⡿⣡⣿⣿⡿⢆
⠿⣿⣧⣤⡘⢿⣿⣿⠏ ⡔⠉⠉⢻⣦⠻⣿⣿⣶⣾⡟⣼⣿⣿⣱⣿⡿⢫⣾⣿
⣷⣮⣝⣛⣃⡉⣿⡏ ⣾⣧  ⣿⡇⢘⣿⠋ ⠻⣿⣿⣿⢟⣵⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣌⢧⣴⣘⢿⣿⣷⣶⡿⠁⢠⠿⠁⠜   ⣸⣿⣿⣿⡿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣦⡙⣿⣷⣉⡛⠋  ⣰⣾⣦⣤⣤⣾⠿⠟⢋⣴⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣌⢿⣿⣿⣿⣿⢰⡿⣻⣿⣿⣿⣿⣿⢃⣰⣫⣾⣿⣿
⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠿⠿⠿⠛⢰⣾⡿⢟⣭⣿⣿⣿⣿⣿⣿⣿⣿⣿""", align=ALIGNMENT, font=('Arial', 12, 'normal'))
