import colorgram
import turtle
import random

tim = turtle.Turtle()

""" THIS SECTION OF CODE IS NOT WORKING AND GIVING AN ERROR"""

# colors = colorgram.extract("hirst_image.jpg", 50)
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r,g,b))
#
# print(rgb_colors)

colours = [
    'old lace', 'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
    'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
    'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
    'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
    'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
    'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
    'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
    'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
    'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
    'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
    'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
    'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
    'indian red', 'saddle brown', 'sandy brown',
    'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange']


tim.width(10)
tim.speed("fastest")
tim.hideturtle()

for i in range(10):
    for j in range(10):
        tim.color(random.choice(colours))
        tim.circle(1)
        tim.penup()
        tim.forward(50)
        tim.pendown()
    if i%2 == 1:
        tim.penup()
        tim.backward(50)
        tim.right(90)
        tim.backward(50)
        tim.right(90)
        tim.pendown()
    else:
        tim.penup()
        tim.backward(50)
        tim.left(90)
        tim.backward(50)
        tim.left(90)
        tim.pendown()


screen = turtle.Screen()
screen.exitonclick()