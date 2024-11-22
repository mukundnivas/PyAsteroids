from random import uniform
import pygame
from CircleShape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        pass

    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,3)
    
    def update(self,dt):
        self.position += self.velocity * dt

    def split(self,dt):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        
        self.kill()

        rotation_angle = uniform(20,50)
        split_asteroid_radius =  self.radius - ASTEROID_MIN_RADIUS
        
        split_asteroid_one = Asteroid(self.position.x,self.position.y,split_asteroid_radius)
        split_asteroid_one.velocity =  1.2 * self.velocity.rotate(rotation_angle)
        
        split_asteroid_two = Asteroid(self.position.x,self.position.y,split_asteroid_radius)
        split_asteroid_two.velocity = 1.2 * self.velocity.rotate(-rotation_angle)