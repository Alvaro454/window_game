import pygame
import random

# interactive.py
pygame.init()

# Box settings
box_size = 50


def add_interactive_elements(window_x, window_y,surface):
    # Modify the position
    box_x = random.randint(0, window_x - box_size)
    box_y = random.randint(0, window_y - box_size)

    try:
        # Load the image
        image = pygame.image.load('Images/email.jpg')
        image = pygame.transform.scale(image, (box_size, box_size))
    except pygame.error as e:
        print(f"Unable to load image: {e}")
        # Create a colored box as a fallback
        image = pygame.Surface((box_size, box_size))
        image.fill((255, 0, 0))

    # Blit the image onto the surface
    surface.blit(image, (box_x, box_y))

    # Create a rectangle for collision detection
    box = pygame.Rect(box_x, box_y, box_size, box_size)

    return image, box