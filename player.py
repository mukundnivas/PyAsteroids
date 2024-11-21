import pygame
from CircleShape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, SHOOT_RATE_LIMIT
from shot import Shot

class Player(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0


    def traingle(self):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        right = pygame.Vector2(0,1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a,b,c]

    def draw(self,screen):
        vertices = self.traingle()
        pygame.draw.polygon(screen,"white",vertices,2)
    
    def update(self,dt):
        keys = pygame.key.get_pressed()
        self.shoot_timer -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)
        
        if keys[pygame.K_w]:
            self.move(dt)
        
        if keys[pygame.K_s]:
            self.move(-dt)
        
        if keys[pygame.K_SPACE]:
            self.shoot(dt)

    def move(self,dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += forward * dt * PLAYER_SPEED

    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def shoot(self,dt):
        if self.shoot_timer > 0:
            return
        self.shoot_timer = SHOOT_RATE_LIMIT
        shot = Shot(self.position.x,self.position.y)
        shot.velocity = pygame.math.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
    