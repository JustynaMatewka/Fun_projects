# import turtle
# from turtle import Screen
#
# pamela = turtle.Turtle()    #new object from a Blueprint
# print(pamela)
# pamela.shape("turtle")  #called method
# pamela.color("DarkOliveGreen4")  #called method
# pamela.forward(100.0)  #called method
#
# my_screen = Screen()    #new object from a Blueprint
# print(my_screen.canvheight) #got the attribute
# my_screen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
