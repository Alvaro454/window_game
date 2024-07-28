import pygame
import sys

#Initialize Pygame
pygame.init()

#Screen dimensions
WIDTH, HEIGHT = 900, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Character Control")

#Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

#Character settings
char_size = 50
char_x, char_y = WIDTH//2, HEIGHT//2
char_speed = 5

#Clock to control frame rate
clock = pygame.time.Clock()

#Main loop
while True:
    #Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    #Handle key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        char_x -= char_speed
        if char_x < 0:
            char_x = 0
    if keys[pygame.K_RIGHT]:
        char_x += char_speed
        if char_x > WIDTH - char_size:
            char_x = WIDTH - char_size
    if keys[pygame.K_UP]:
        char_y -= char_speed
        if char_y < 0:
            char_y = 0
    if keys[pygame.K_DOWN]:
        char_y += char_speed
        if char_y > HEIGHT - char_size:
            char_y = HEIGHT - char_size

    #Fill screen with white
    screen.fill(WHITE)

    #Draw character(a blue square)
    pygame.draw.rect(screen, BLUE, (char_x, char_y, char_size, char_size))
    pygame.display.flip()
    # Restrict character movement within screen boundaries
    
    clock.tick(30)

##
import tkinter as tk

def create_window(title, color):
    new_window = tk.Toplevel(root)  # Create a new top-level window
    new_window.title(title)
    new_window.geometry("400x300")
    new_window.configure(bg=color)
    label = tk.Label(new_window, text=title, bg=color, fg="white")
    label.pack(expand=True)

# Main window setup
root = tk.Tk()
root.title("Main Window")
root.geometry("400x300")

# Create buttons to open new windows
button1 = tk.Button(root, text="Open Window 1", command=lambda: create_window("Window 1", "blue"))
button1.pack(pady=10)

button2 = tk.Button(root, text="Open Window 2", command=lambda: create_window("Window 2", "green"))
button2.pack(pady=10)

root.mainloop()