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
    if keys[pygame.K_RIGHT]:
        char_x += char_speed
    if keys[pygame.K_UP]:
        char_y -= char_speed
    if keys[pygame.K_DOWN]:
        char_y += char_speed

    #Fill screen with white
    screen.fill(WHITE)

    #Draw character(a blue square)
    pygame.draw.rect(screen, BLUE, (char_x, char_y, char_size, char_size))
    pygame.display.flip()

    clock.tick(30)