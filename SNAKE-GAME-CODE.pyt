import tkinter
import random  

ROWS = 25
COLS = 25
TILE_SIZE = 25

WINDOW_WIDTH = TILE_SIZE * COLS
WINDOW_HEIGHT = TILE_SIZE * ROWS

class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

window = tkinter.Tk()
window.title("🐍 Snake Game")
window.resizable(False, False)

canvas = tkinter.Canvas(
    window, bg="black", width=WINDOW_WIDTH, height=WINDOW_HEIGHT,
    borderwidth=0, highlightthickness=0
)
canvas.pack()
window.update()

snake = Tile(TILE_SIZE * 5, TILE_SIZE * 5)
food = Tile(TILE_SIZE * 10, TILE_SIZE * 10)
velocityX = 0
velocityY = 0
snake_body = []
game_over = False
score = 0
game_speed = 100  

def reset_game():
    global snake, food, velocityX, velocityY, snake_body, game_over, score, game_speed
    snake = Tile(TILE_SIZE * 5, TILE_SIZE * 5)
    food = Tile(TILE_SIZE * 10, TILE_SIZE * 10)
    velocityX = 0
    velocityY = 0
    snake_body = []
    game_over = False
    score = 0
    game_speed = 100
    draw()

def change_direction(e):
    global velocityX, velocityY, game_over
    if game_over:
        if e.keysym == "Return":  # Press Enter to restart
            reset_game()
        return

    if e.keysym == "Up" and velocityY != 1:
        velocityX = 0
        velocityY = -1
    elif e.keysym == "Down" and velocityY != -1:
        velocityX = 0
        velocityY = 1
    elif e.keysym == "Left" and velocityX != 1:
        velocityX = -1
        velocityY = 0
    elif e.keysym == "Right" and velocityX != -1:
        velocityX = 1
        velocityY = 0

def increase_speed():
    global game_speed
    if game_speed > 40:  
        game_speed -= 10

def move():
    global snake, food, snake_body, game_over, score

    if game_over:
        return

    if (snake.x < 0 or snake.x >= WINDOW_WIDTH or snake.y < 0 or snake.y >= WINDOW_HEIGHT):
        game_over = True
        return

    for tile in snake_body:
        if snake.x == tile.x and snake.y == tile.y:
            game_over = True
            return

    if snake.x == food.x and snake.y == food.y:
        snake_body.append(Tile(food.x, food.y))
        food.x = random.randint(0, COLS - 1) * TILE_SIZE
        food.y = random.randint(0, ROWS - 1) * TILE_SIZE
        score += 1
        if score % 5 == 0:
            increase_speed()

    for i in range(len(snake_body) - 1, -1, -1):
        tile = snake_body[i]
        if i == 0:
            tile.x = snake.x
            tile.y = snake.y
        else:
            prev = snake_body[i - 1]
            tile.x = prev.x
            tile.y = prev.y

    snake.x += velocityX * TILE_SIZE
    snake.y += velocityY * TILE_SIZE

def draw():
    global snake, food, snake_body, game_over, score
    move()

    canvas.delete("all")
    canvas.create_rectangle(food.x, food.y, food.x + TILE_SIZE, food.y + TILE_SIZE, fill='red')
    canvas.create_rectangle(snake.x, snake.y, snake.x + TILE_SIZE, snake.y + TILE_SIZE, fill='lime green')
    for tile in snake_body:
        canvas.create_rectangle(tile.x, tile.y, tile.x + TILE_SIZE, tile.y + TILE_SIZE, fill='lime green')
    canvas.create_text(40, 20, font="Arial 12 bold", text=f"Score: {score}", fill="white")
    if game_over:
        canvas.create_text(WINDOW_WIDTH/2, WINDOW_HEIGHT/2 - 20, font="Arial 20 bold", text=f"Game Over!", fill="white")
        canvas.create_text(WINDOW_WIDTH/2, WINDOW_HEIGHT/2 + 10, font="Arial 16", text=f"Your Score: {score}", fill="yellow")
        canvas.create_text(WINDOW_WIDTH/2, WINDOW_HEIGHT/2 + 40, font="Arial 12", text="Press ENTER to Restart", fill="cyan")
    else:
        window.after(game_speed, draw)
draw()
window.bind("<KeyRelease>", change_direction)
window.mainloop()
