import tkinter as tk
import random

# # ---------------DECLARATION  CONSTANTS ----------------
# GRID_SIZE اندازه هر واحد از صفحه بازی (مانند یک مربع) را نشان می‌دهد.
GRID_SIZE = 20
WIDTH, HEIGHT = 400, 400
SNAKE_SIZE = 20
START_SPEED = 150

class SnakeGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Snake Game")
        self.canvas = tk.Canvas(self.root, width=WIDTH, height=HEIGHT)
        self.canvas.pack()

        self.snake = [(100, 100)]    #self.snake یک لیست از موقعیت‌های تمام بخش‌های بدن مار است.
        self.food = self.generate_food()
        self.direction = "Right"
        self.speed = START_SPEED

        self.root.bind("<KeyPress>", self.change_direction)

        self.update()

        self.root.mainloop()

    def generate_food(self):
        x = random.randint(0, (WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
        y = random.randint(0, (HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
        return x, y

    def change_direction(self, event):
        key = event.keysym
        if key == "Up" and self.direction != "Down":
            self.direction = "Up"
        elif key == "Down" and self.direction != "Up":
            self.direction = "Down"
        elif key == "Left" and self.direction != "Right":
            self.direction = "Left"
        elif key == "Right" and self.direction != "Left":
            self.direction = "Right"

    def move_snake(self):
        head_x, head_y = self.snake[0]    #This line extracts the coordinates of the snake's head from the self.snake list and stores them in the head_x and head_y variables.
        if self.direction == "Up":
            new_head = (head_x, head_y - GRID_SIZE)  #Creates a new tuple that shows the coordinates of the snake's head after moving.
        elif self.direction == "Down":
            new_head = (head_x, head_y + GRID_SIZE)
        elif self.direction == "Left":
            new_head = (head_x - GRID_SIZE, head_y)
        elif self.direction == "Right":
            new_head = (head_x + GRID_SIZE, head_y)

        # Check for collisions
        if new_head in self.snake or not (0 <= new_head[0] < WIDTH and 0 <= new_head[1] < HEIGHT):
            self.game_over()
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.food = self.generate_food()
            self.speed -= 2

        else:
           self.snake.pop()

        self.draw_game()    # update the game

        self.root.after(self.speed, self.move_snake)   # after decrease speed run the movesnake func

    def draw_game(self):
        self.canvas.delete(tk.ALL)
        # create rectangle 
        self.canvas.create_rectangle(*self.food, self.food[0] + GRID_SIZE, self.food[1] + GRID_SIZE, fill="red")
        # This part calculates the bottom right corner of the rectangle by adding GRID_SIZE to the food coordinates (specifies the total size of the rectangle).
    
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x + SNAKE_SIZE, y + SNAKE_SIZE, fill="black")

    def game_over(self):
        self.canvas.delete(tk.ALL)
        self.canvas.create_text(WIDTH // 2, HEIGHT // 2, text="Game Over", font=("Helvetica", 32), fill="red")

    def update(self):
        self.move_snake()

if __name__ == "__main__":
    game = SnakeGame()