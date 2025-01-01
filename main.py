import pygame
from constants import *
from player import *
from asteroid import *
from AsteroidField import *
from shot import *
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    timeclock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)
    asteroidfield = AsteroidField()
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen,(0,0,0))
        timeclock.tick(60)
        dt= timeclock.tick(60)/1000
        for obj in updatable: 
             obj.update(dt)
        
        for obj in asteroids:
             if obj.collision(player):
                  print(f"Game over!")
                  sys.exit()
             for shot in shots:
                  if obj.collision(shot):
                     obj.split()
                     shot.kill()

        for obj in drawable:
             obj.draw(screen)
        

        
        pygame.display.flip()
        
        

if __name__ == "__main__":
        main()
