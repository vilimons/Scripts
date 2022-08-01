import turtle as turtle_module
import random


tim = turtle_module.Turtle()
turtle_module.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()


color_list = [(202, 164, 164), (149, 75, 75), (222, 201, 201), (53, 93, 93), (170, 154, 154), (138, 31, 31), (134, 163, 163), (197, 92, 92), (47, 121, 121), (73, 43, 43), (145, 178, 178), (14, 98, 98), (232, 176, 176), (160, 142, 142), (54, 
45, 45), (101, 75, 75), (183, 205, 205), (36, 60, 60), (19, 86, 86), (82, 
148, 148), (147, 17, 17), (27, 68, 68), (12, 70, 70), (107, 127, 127), (176, 192, 192), (168, 99, 99)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



screen = turtle_module.Screen()
screen.exitonclick()