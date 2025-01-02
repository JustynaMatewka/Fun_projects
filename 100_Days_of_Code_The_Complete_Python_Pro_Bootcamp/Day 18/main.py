import turtle, random, colorgram

# colors = colorgram.extract('image.jpg', 45)
# rgb_colors = []
#
# for color in colors:
#     rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))
# print(rgb_colors)

colors_list = [(232, 241, 239), (1, 9, 30), (229, 235, 242), (239, 232, 238), (121, 95, 41), (72, 32, 21), (238, 212, 72), (220, 81, 59), (226, 117, 100), (93, 1, 21), (178, 140, 170), (151, 92, 115), (35, 90, 26), (6, 154, 73), (205, 63, 91), (168, 129, 78), (3, 78, 28), (1, 64, 147), (221, 179, 218), (4, 220, 218), (80, 135, 179), (130, 157, 177), (81, 110, 135), (120, 187, 164), (11, 213, 220), (118, 18, 36), (243, 205, 7), (132, 223, 209), (229, 173, 165), (70, 70, 45), (185, 190, 201), (126, 225, 231), (88, 49, 45), (61, 65, 66)]
number_of_dots = 100
turtle.colormode(255)
my_turtle = turtle.Turtle()
my_turtle.speed("fastest")
my_turtle.penup()
my_turtle.hideturtle()
my_turtle.goto(-300, -300)

for dot_count in range(number_of_dots):
    if dot_count % 10 == 0 and dot_count > 1:
        my_turtle.right(180)
        my_turtle.forward(450)
        my_turtle.right(90)
        my_turtle.forward(50)
        my_turtle.right(90)
    else:
        my_turtle.forward(50)
    my_turtle.dot(20, random.choice(colors_list))


screen = turtle.Screen()
screen.exitonclick()