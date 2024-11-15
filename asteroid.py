import pygame
from CircleShape import CircleShape

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        pass

    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,3)
    
    def update(self,dt):
        self.position += self.velocity * dt
