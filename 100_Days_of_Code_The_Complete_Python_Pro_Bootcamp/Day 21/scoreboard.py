from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.value = 0
        self.increase_score()

    def increase_score(self):
        self.clear()
        self.update_scoreboard()
        self.value += 1

    def update_scoreboard(self):
        self.write(arg=f"Score: {self.value}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", move=False, align=ALIGNMENT, font=FONT)
