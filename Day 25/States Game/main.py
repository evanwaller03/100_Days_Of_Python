import pandas
import turtle

FONT = ("Courier", 10, "normal")

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "/Users/evanwaller/Desktop/GitHub Projects/100 Days of Code/Day 25/States Game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guess_list = []
missing_states = []

data = pandas.read_csv("Day 25/States Game/50_states.csv")
all_states = data.state.to_list()

def already_guessed(user_input):

    for guess in guess_list:
        if user_input == guess:
            return True
    guess_list.append(user_input)
    return False


def is_a_state(user_input):

    for state in data["state"]:
        if state == user_input:
            return True
    return False

def guess_is_right(state):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()

    state_data = data[data.state == state]
    t.goto(int(state_data.x), int(state_data.y))
    t.write(f"{state}", font=FONT)

while len(guess_list) != 50:
    state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
    if state == "exit":
        missing_states = [state for state in all_states if state not in guess_list]
        
        print(missing_states)
        break
    if is_a_state(state):
        if not(already_guessed(state)):
            guess_is_right(state)
