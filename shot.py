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