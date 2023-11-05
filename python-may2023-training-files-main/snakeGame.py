""" Snake Game """

# Importing Modules
import random
import colorama
from pynput import keyboard
import time
import threading
import os


# Stop color propagation
colorama.init(autoreset=True)

WIDTH = 42
HEIGHT = 12
TargetX = random.randint(2, WIDTH-1)
TargetY = random.randint(2, HEIGHT-1)
SnakeX = WIDTH // 2
SnakeY = HEIGHT // 2
SnakeDIR = "right"
DIRECTIONS = {"right":(1, 0), "left":(-1, 0), "up":(0, -1), "down":(0, 1)}
GAMEOVER = False
Score = 0

def sketch():
    for i in range(1, HEIGHT + 1):
        for j in range(1, WIDTH + 1):
            if i == 1 or i == HEIGHT:
                print("-", end='')
            elif i == SnakeY and j == SnakeX:
                print(colorama.Fore.GREEN + "🎃", end='')
            elif i == TargetY and j == TargetX:
                print(colorama.Fore.RED + "🍓", end='')
            elif j == 1 or j == WIDTH:
                print("|", end='')
            else:
                print(" ", end='')
        print()


def input():
    def on_press(key):
        global SnakeDIR
        if key == keyboard.Key.up:
            SnakeDIR = "up"
        elif key == keyboard.Key.down:
            SnakeDIR = "down"
        elif key == keyboard.Key.left:
            SnakeDIR = "left"
        elif key == keyboard.Key.right:
            SnakeDIR = "right"
        else:
            return 0

    while not GAMEOVER:
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()
    
def update():
    global SnakeX, SnakeY, SnakeDIR, TargetX, TargetY, Score, GAMEOVER
    SnakeX += DIRECTIONS[SnakeDIR][0]
    SnakeY += DIRECTIONS[SnakeDIR][1]

    if SnakeX == TargetX and SnakeY == TargetY:
        Score += 1
        TargetX = random.randint(2, WIDTH - 1)
        TargetY = random.randint(2, HEIGHT - 1)
    elif SnakeX == 1 or SnakeX == WIDTH or SnakeY == 1 or SnakeY == HEIGHT:
        GAMEOVER = True
    else:
        return 0


thread = threading.Thread(target=input)
thread.start()

while not GAMEOVER:
    print(f"SCORE :- {Score}")
    sketch()
    update()
    time.sleep(0.3)
    os.system('cls')
del thread
print(colorama.Fore.YELLOW + "GAME OVER!!!")
print(colorama.Fore.GREEN + f"Total Score :- {Score}")