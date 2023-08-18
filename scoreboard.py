from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.speed("fastest")
        self.color("white")
        self.penup()
        self.goto(0, 275)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", False, "center", ('Arial', 15, 'normal'))

    def refresh(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.home()
        self.write(f"GAME OVER", False, "center", ('Arial', 25, 'normal'))
