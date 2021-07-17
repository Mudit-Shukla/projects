import turtle
import pandas

screen = turtle.Screen()
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)
game_is_on = True
score = 0

def write_states(state, x, y):
    new_turtle = turtle.Turtle()
    new_turtle.penup()
    new_turtle.hideturtle()
    new_turtle.goto(x, y)
    new_turtle.write(f"{state}", align="center", font = ("Arial", 10, "normal"))

while game_is_on:
    answer_state = screen.textinput(f"Guess the state {score}/50", "Name any of the remaining states")
    data = pandas.read_csv("../../../../Udemy python course 1/projects/usstatesgame/50_states.csv")
    list_of_states = data.state.to_list()
    if answer_state in list_of_states:
        score += 1
        state_data = data[data["state"] == answer_state]
        latitude, longitude = state_data["x"], state_data["y"]
        write_states(answer_state, int (latitude), int (longitude))
        if score >= 50:
            game_is_on = False

    else:
        pass
screen.mainloop()