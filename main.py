import turtle as turtle_module
import random
turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.penup()
tim.hideturtle()
color_list = [(198, 13, 32), (248, 236, 26), (40, 77, 188), (227, 159, 51), (40, 217, 70), (238, 227, 5), (242, 246, 252), (29, 39, 154), (212, 75, 15), (17, 153, 17), (222, 21, 119), (194, 15, 11), (240, 38, 162), (68, 10, 31), (221, 141, 203), (60, 15, 9), (11, 97, 63), (55, 209, 230), (218, 159, 11), (17, 19, 49), (235, 158, 214), (77, 212, 165), (84, 76, 209), (11, 227, 238), (106, 230, 194), (217, 87, 50), (6, 67, 42)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100
for dot_count in range(1, number_of_dots+1):
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
