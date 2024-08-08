import pygame
import random
import main

# interactive.py
pygame.init()


# Box settings
box_size = 50


def add_interactive_elements():
    # Create an immovable box
    box = pygame.Rect(100, 100, box_size, box_size)

    # Access the position
    print(f"Box position: {box.topleft}")

    # Modify the position
    box.x = random.randint(0, main.current_window.width - box_size)
    box.y = random.randint(0, main.current_window.height - box_size)
    print(f"New box position: {box.topleft}")
