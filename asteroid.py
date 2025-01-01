from circleshape import *
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
    
    def update(self, dt):
        self.position += (self.velocity * dt) 
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20,50)
            #new_radius = self.radius - ASTEROID_MIN_RADIUS
            #position = self.position
            Asteroid(self.position[0],self.position[1], self.radius - ASTEROID_MIN_RADIUS).velocity = self.velocity.rotate(angle)
            Asteroid(self.position[0],self.position[1], self.radius - ASTEROID_MIN_RADIUS).velocity = self.velocity.rotate(-angle)


            

            




