import pygame
import ctypes
import sys
from interactive import add_interactive_elements

# Initialize Pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)

# Character settings
char_size = 50
char_speed = 5

# Clock to control frame rate
clock = pygame.time.Clock()

class Window:
    def __init__(self, title, color, width, height):
        self.title = title
        self.color = color
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)
    
    def center_window(self):
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)

        # Get the screen width and height
        user32 = ctypes.windll.user32
        screen_width = user32.GetSystemMetrics(0)  # Get screen width
        screen_height = user32.GetSystemMetrics(1)  # Get screen height
        
        # Calculate the position to center the window
        x = (screen_width - self.width) // 2
        y = (screen_height - self.height) // 2
        
        # Move the window to the center
        hwnd = pygame.display.get_wm_info()['window']
        ctypes.windll.user32.MoveWindow(hwnd, x, y, self.width, self.height, True)
    
    def update(self):
        self.screen.fill(self.color)
        pygame.display.flip()
        pygame.display.set_caption(self.title)

def main():
    global screen, current_window
    i=0
    current_window = Window("Main Window", WHITE, 900, 500)
    char_x, char_y = current_window.width // 2, current_window.height // 2

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        # Check if the character touches the borders
        if char_x < 0:  # Left border
            char_x = 0
            current_window = Window("Window 1", BLUE, 1000, 500)
            current_window.center_window()
            char_x, char_y = current_window.width - char_size, current_window.height // 2
            i=0
        elif char_x > current_window.width - char_size:  # Right border
            char_x = current_window.width - char_size
            current_window = Window("Window 2", RED, 1500, 700)
            current_window.center_window()
            char_x, char_y = 0, current_window.height // 2
            i=0
        elif char_y < 0:  # Top border
            char_y = 0
            current_window = Window("Window 3", PURPLE, 800, 600)
            current_window.center_window()
            char_x, char_y = current_window.width // 2, current_window.height - char_size
            i=0
        elif char_y > current_window.height - char_size:  # Bottom border
            char_y = current_window.height - char_size
            current_window = Window("Window 4", YELLOW, 1200, 800)
            current_window.center_window()
            char_x, char_y = current_window.width // 2, 0
            i=0
        
        # Control character
        if keys[pygame.K_LEFT]:
            char_x -= char_speed
        if keys[pygame.K_RIGHT]:
            char_x += char_speed
        if keys[pygame.K_UP]:
            char_y -= char_speed
        if keys[pygame.K_DOWN]:
            char_y += char_speed

        # Update the current window
        current_window.update()
        
        # Draw the character
        pygame.draw.rect(current_window.screen, GREEN, (char_x, char_y, char_size, char_size))
        pygame.display.flip()

        if i == 0:
            # Add interactive elements
            box=add_interactive_elements(current_window.width, current_window.height)
            i=1
        pygame.draw.rect(current_window.screen, (0, 128, 255), box)
        pygame.display.flip()

        clock.tick(30)

if __name__ == "__main__":
    main()