import pygame
from circleshape import CircleShape
from constants import *
class Shot(CircleShape):
    def __init__(self, x, y):
        self.radius = SHOT_RADIUS
        self.velocity = PLAYER_SHOOT_SPEED
        super().__init__(x, y, self.radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
    
    def update(self, dt):
        self.position += (self.velocity * dt) 
        