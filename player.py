from circleshape import CircleShape
from constants import *
import pygame

class Player(CircleShape):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, PLAYER_RADIUS)
        self.position = pygame.Vector2(x, y)
        self.rotation = 0
        
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
        
    def rotate(self, dt: float, clockwise: bool):
        direction = 1 if clockwise else -1
        self.rotation += PLAYER_TURN_SPEED * dt * direction
        
    def move(self, dt: float, forward: bool):
        direction = 1 if forward else -1
        self.position += pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SPEED * dt * direction
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)
        
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt, False)
        if keys[pygame.K_d]:
            self.rotate(dt, True)
        if keys[pygame.K_w]:
            self.move(dt, True)
        if keys[pygame.K_s]:
            self.move(dt, False)