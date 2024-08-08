import pygame
import random

# interactive.py
pygame.init()

# Box settings
box_size = 50


def add_interactive_elements(window_x, window_y):
    # Modify the position
    box_x = random.randint(0, window_x - box_size)
    box_y = random.randint(0, window_y - box_size)

    # Create an immovable box
    box = pygame.Rect(box_x, box_y, box_size, box_size)

    return box
