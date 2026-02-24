import turtle
import pandas
from tkinter import messagebox

screen = turtle.Screen()
screen.title("US State Game")
image = "blank_states_img.gif"
screen.addshape(image)
#shows the map
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = set()

messagebox.showinfo(
    title="Welcome",
    message="Guess the U.S. states.\n\nType 'Exit' anytime to end the game."
)

while len(guessed_states) < len(all_states):
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name?"
    )

    if answer_state is None:
        continue

    answer_state = answer_state.title()

    if answer_state == "Exit":
        break
    if answer_state in all_states:
        guessed_states.add(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_data.state.item())
    else:
        messagebox.showinfo(
            title="Try Again",
            message="That doesn't look like a U.S. state.\nKeep going — you’ve got this!"
        )

# --- Save missed states ---
missed_states = [state for state in all_states if state not in guessed_states]
missed_df = pandas.DataFrame(missed_states, columns=["Missed States"])
missed_df.to_csv("missed_states.csv", index=False)

messagebox.showinfo(
    title="Game Over",
    message=f"You missed {len(missed_states)} states.\nThey are saved in missed_states.csv"
)

screen.bye()  # Close the turtle window