from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.paddle_segments = []
        x_pos = 350
        y_pos = -50
        super().__init__()
        self.color("pink")
        self.penup()
        self.shape("square")
        self.speed("fastest")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def r_move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def r_move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def l_move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def l_move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)