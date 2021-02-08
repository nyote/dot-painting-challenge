#Creating a hirst-like art
#First extracting colors by using a colorgram package

# import colorgram
# colors = True
# color_list = []
# color_number = 30
# extracted_colors = colorgram.extract("damien-hirst-the-complete-spot-paintings-1986-2011-46.gif", 30)
# for color in extracted_colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_info = (r, g, b)
#     color_list.append(color_info)

#print(color_list)

### got the list here: color_list_tuples = [(239, 67, 34), (236, 35, 119), (152, 27, 62), (6, 150, 96), (238, 209, 222), (206, 224, 230), (245, 166, 34), (44, 190, 232), (183, 158, 46), (27, 127, 195), (126, 193, 74), (86, 28, 94), (250, 221, 21), (255, 223, 0), (179, 39, 105), (217, 135, 162), (92, 179, 91), (227, 169, 190), (141, 209, 229), (240, 163, 152), (170, 206, 166), (167, 56, 55), (0, 126, 51), (190, 185, 202)]
### now as the second part, I will be using this color list that was extracted to generate

import turtle as t
import random as random

color_list_tuples = [(239, 67, 34), (236, 35, 119), (152, 27, 62), (6, 150, 96), (238, 209, 222), (206, 224, 230), (245, 166, 34), (44, 190, 232), (183, 158, 46), (27, 127, 195), (126, 193, 74), (86, 28, 94), (250, 221, 21), (255, 223, 0), (179, 39, 105), (217, 135, 162), (92, 179, 91), (227, 169, 190), (141, 209, 229), (240, 163, 152), (170, 206, 166), (167, 56, 55), (0, 126, 51), (190, 185, 202)]

tim_turtle = t
tim_turtle.penup()
tim_turtle.setpos(-200, -200)
tim_turtle_screen = tim_turtle.Screen()
list_size = len(color_list_tuples)
tim_turtle_screen.colormode(255)
tim_turtle_screen.screensize(1000, 1000)
circles_amount = 1
for _ in range(100):

    tim_turtle.pendown()
    tim_turtle.pensize(20)
    color_tim = color_list_tuples[random.randint(0, list_size - 1)]
    print(circles_amount)
    tim_turtle.pencolor(color_tim)
    tim_turtle.dot()
    tim_turtle.penup()
    tim_turtle.forward(50)
    if circles_amount % 20 == 0:
        tim_turtle.right(90)
        tim_turtle.pendown()
        tim_turtle.dot()
        tim_turtle.penup()
        tim_turtle.forward(50)
        tim_turtle.right(90)
    elif circles_amount % 10 == 0 and circles_amount % 20 != 0:
        tim_turtle.left(90)
        tim_turtle.pendown()
        tim_turtle.dot()
        tim_turtle.penup()
        tim_turtle.forward(50)
        tim_turtle.left(90)
    circles_amount += 1






tim_turtle_screen.exitonclick()