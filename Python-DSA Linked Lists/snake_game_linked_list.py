# Snake Game
# Using linked list
from tkinter import *
import random

# Screen Size
width = 500
height = 500
space_size = 20
background = "white"
# Snake 
speed = 200
body_size = 2
snake = "red"
food = "green"


# Modify the snake in the game
class Snake:
    def __init__(self):
        self.body_size = body_size
        self.coordinates = []
        self.squares = []

        for i in range(0, body_size):
            self.coordinates.append([0, 0])

        for xi, yi in self.coordinates:
            square = canvas.create_rectangle(xi, yi, xi + space_size,
                                             yi + space_size, fill=snake, tag="snake")
            self.squares.append(square)


class Food:
    def __init__(self):
        self.coordinates = None
        self.move()

    def move(self):  # Move the food
        canvas.delete("food")
        # Food at random position
        a = random.randint(0, (width // space_size) - 1) * space_size
        b = random.randint(0, (height // space_size) - 1) * space_size
        self.coordinates = [a, b]
        canvas.create_oval(a, b, a + space_size,
                           b + space_size, fill=food, tag="food")


# Check all the snake moves
def next_turn(game_snake, game_food):
    x_axis, y_axis = game_snake.coordinates[0]

    if direction == "up":
        y_axis -= space_size
    elif direction == "down":
        y_axis += space_size
    elif direction == "left":
        x_axis -= space_size
    elif direction == "right":
        x_axis += space_size

    game_snake.coordinates.insert(0, (x_axis, y_axis))
    square = canvas.create_rectangle(x_axis, y_axis, x_axis + space_size,
                                     y_axis + space_size, fill=snake)
    game_snake.squares.insert(0, square)

    if x_axis == game_food.coordinates[0] and y_axis == game_food.coordinates[1]:
        global score
        score += 1
        label.config(text="Points:{}".format(score))
        game_food.move()

    else:
        del game_snake.coordinates[-1]
        canvas.delete(game_snake.squares[-1])
        del game_snake.squares[-1]

    if check_collisions(game_snake):
        game_over()
    else:
        window.after(speed, next_turn, game_snake, game_food)


def change_direction(new_direction):
    global direction
    if new_direction == "left":
        if direction != "right":
            direction = new_direction
    elif new_direction == "right":
        if direction != "left":
            direction = new_direction
    elif new_direction == "up":
        if direction != "down":
            direction = new_direction
    elif new_direction == "down":
        if direction != "up":
            direction = new_direction


# Check for collision 
def check_collisions(game_snake):
    m, n = game_snake.coordinates[0]

    if m < 0 or m >= width:
        return True
    elif n < 0 or n >= height:
        return True

    for body_part in game_snake.coordinates[1:]:
        if m == body_part[0] and n == body_part[1]:
            return True

    return False


def game_over():  # When game over
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2,
                       font=('consolas', 70),
                       text="GAME OVER", fill="red", tag="gameover")


# Game Screen Title
window = Tk()
window.title("Snake Game")

score = 0
direction = "down"

# Display the score
label = Label(window, text="Points:{}".format(score),
              font=("consolas", 20))
label.pack()

canvas = Canvas(window, bg=background, height=height, width=width)
canvas.pack()

window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")
window.bind("<Left>", lambda event: change_direction("left"))
window.bind("<Right>", lambda event: change_direction("right"))
window.bind("<Up>", lambda event: change_direction("up"))
window.bind("<Down>", lambda event: change_direction("down"))

Snake = Snake()
Food = Food()
next_turn(Snake, Food)


window.mainloop()
