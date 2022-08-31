import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
screen.setup(width=800, height=550)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
correct = 0

data = pandas.read_csv("50_states.csv")
info = data.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
    answer = screen.textinput(title=f"{len(guessed_state)}/50 States Correct", prompt="What's another states name?").title()

    if answer == "Exit":
        missing_state = []
        for state in info:
            if state not in guessed_state:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer in info:
        guessed_state.append(answer)
        pos = turtle.Turtle()
        pos.hideturtle()
        pos.penup()
        state_data = data[data.state == answer]
        pos.goto(int(state_data.x), int(state_data.y))
        pos.write(f"{answer}", font=("Courier", 6, "bold"))



