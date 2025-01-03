from turtle import Turtle, Screen

my_turtle = Turtle()
screen = Screen()

def w_move_forward():
    my_turtle.forward(10)

def s_move_backwards():
    my_turtle.backward(10)

def a_turn_left():
    my_turtle.left(10)

def d_turn_right():
    my_turtle.right(10)

def c_clear_screen():
    my_turtle.clear()
    my_turtle.penup()
    my_turtle.home()
    my_turtle.pendown()


screen.listen()
screen.onkey(key="w", fun=w_move_forward)
screen.onkey(key="s", fun=s_move_backwards)
screen.onkey(key="a", fun=a_turn_left)
screen.onkey(key="d", fun=d_turn_right)
screen.onkey(key="c", fun=c_clear_screen)
screen.exitonclick()

