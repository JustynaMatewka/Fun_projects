from turtle import Turtle, Screen
import random


def random_color():
    r = random.random()
    b = random.random()
    g = random.random()
    return r, b, g


pamela_the_turtle = Turtle()
pamela_the_turtle.shape("turtle")
pamela_the_turtle.color("DarkOliveGreen4")


#   Turtle draw a square
# for _ in range(4):
#     pamela_the_turtle.forward(100)
#     pamela_the_turtle.right(90)


#   Turtle draw dashed line
# for _ in range(15):
#     pamela_the_turtle.forward(10)
#     pamela_the_turtle.penup()
#     pamela_the_turtle.forward(10)
#     pamela_the_turtle.pendown()


#   Turtle draw triangle, square, (...), nonagon and decagon from the same point
# for nr_walls in range(3, 10):
#     turn = 360 // nr_walls
#     pamela_the_turtle.pencolor(random_color())
#
#     for _ in range(nr_walls):
#         pamela_the_turtle.forward(100)
#         pamela_the_turtle.right(turn)


#   Turtle random walk
# directions = [0, 90, 180, 270]
# pamela_the_turtle.pensize(10)
# pamela_the_turtle.speed(10)
#
# for _ in range(500):
#     pamela_the_turtle.pencolor(random_color())
#     pamela_the_turtle.forward(20)
#     this_turn = random.choice(directions)
#     pamela_the_turtle.right(this_turn)


#   Turtle draw a Spirograph
direction = 0
pamela_the_turtle.speed("fastest")

for _ in range(72):
    pamela_the_turtle.setheading(direction)
    pamela_the_turtle.pencolor(random_color())
    pamela_the_turtle.circle(100)
    direction += 5


screen = Screen()
screen.exitonclick()
