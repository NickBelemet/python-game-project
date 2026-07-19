import pygame, sys
from game import Game

# Initialize Pygame
pygame.init()
dark_purple = (170, 0, 250)


screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

game = Game()

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit() 
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_LEFT:
                game.move_left()
            elif event.key == pygame.K_RIGHT:
                game.move_right()
            elif event.key == pygame.K_DOWN:
                game.move_down()

    #Screen drawing        
    screen.fill(dark_purple)
    game.draw(screen)
    pygame.display.update()
    clock.tick(60)  #frame rate of 60 

 