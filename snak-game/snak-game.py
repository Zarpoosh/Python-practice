from tkinter import *
import random

# ---------------DECLARATION  CONSTANTS ----------------
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPACE_SIZE = 50
BODY_PARTS=3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000"


# !-------------------snak class------------------------
class Snake:
    def __init__(self):
        self.body_size=BODY_PARTS
        self.coordinates = []
        self.squares=[]
        
        for i in range(0, BODY_PARTS):
            self.coordinates([0,0])      
            
        for x,y in self.coordinates:
            square=canvas.create_rectangle(x,y,x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR, tag="snak")


# !-------------------food class------------------------
class Food:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x, y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

def next_turn():
    pass

def change_direction(new_direction):
    pass

def check_collisions():
    pass

def game_over():
    pass

def on_canvas_resized(event):
    global window_width, window_height, x, y
    window_width = event.width
    window_height = event.height
    x = int((screen_width/2) - (window_width/2))
    y = int((screen_height/2) - (window_height/2))
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window = Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = "down"

label = Label(window, text="Score: {}".format(score), font=("consolas", 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_WIDTH, width=GAME_HEIGHT)
canvas.pack()

window.update()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window.winfo_reqwidth()/2))
y = int((screen_height/2) - (window.winfo_reqheight()/2))

window.geometry(f"{window.winfo_reqwidth()}x{window.winfo_reqheight()}+{x}+{y}")

food = Food()

canvas.bind("<Configure>", on_canvas_resized)
window.mainloop()
