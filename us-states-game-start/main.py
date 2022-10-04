import pandas
import turtle

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
screen.title("States Guessing game")
turtle.shape(image)

states_data = pandas.read_csv("50_states.csv")


def write_name(state):
    state_row = states_data[states_data.state == state]
    x_cor = int(state_row.x)
    y_cor = int(state_row.y)
    writer = turtle.Turtle()
    writer.hideturtle()
    writer.penup()
    writer.goto((x_cor, y_cor))
    writer.pendown()
    writer.write(f"{state}", align="center", font=("Arial", 7, "normal"))

guessed_states = []

while len(guessed_states) < 50:
    answer = screen.textinput(f"{len(guessed_states)}/50 correct states ", "Enter the name of another State").title()
    states_list = states_data.state.to_list()

    if answer in states_list:
        write_name(answer)
        guessed_states.append(answer)
    elif answer == "Exit":
        missed_states = [item for item in states_list if item not in guessed_states]
        # missed_states = []
        # for item in states_list:
        #     if item not in guessed_states:
        #         missed_states.append(item)

        missed_df = pandas.DataFrame(missed_states)
        missed_csv = missed_df.to_csv("states_to_learn.csv")
        break
    else:
        print("Noo")


