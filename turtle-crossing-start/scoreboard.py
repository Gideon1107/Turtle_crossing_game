from turtle import Turtle
FONT = ("Courier", 14, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def increase_level(self):
        self.level += 1

    def update_scoreboard(self):
        self.clear()
        self.goto(-278, 278)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.color("black")
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=("Courier", 14, "normal"))



