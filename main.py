import pygame, sys

# Initialize Pygame
pygame.init()

screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit() 

    pygame.display.update()
    clock.tick(60)  # Limit the frame rate to 60 frames per second