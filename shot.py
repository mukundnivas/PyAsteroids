import pygame
from CircleShape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,SHOT_RADIUS)

    current_time = pygame.time.get_ticks()
    
    def draw(self,screen):      
        pygame.draw.circle(screen,"white",self.position,SHOT_RADIUS,10)
    
    def update(self,dt):
        self.position += self.velocity * dt


"""
split the asteroid

- if shot.collision(asteroid) -> True:
    asteroid.split()

- asteroid.split() -> return sprites
and if the asteroid radius is the min kill em!

The sprite would be an asteroid of radius - 1. Same radius, but position rotate by +45 and -45 so the asteroids are complementry to each other
"""