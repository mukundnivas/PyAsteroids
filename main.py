import pygame
from player import Player
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    game_state = True
    dt = 0
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

    while game_state:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0,0,0))
        player.draw(screen)
        pygame.display.flip()
        dt = game_clock.tick(60) / 1000
    
if __name__ == "__main__":
    main()