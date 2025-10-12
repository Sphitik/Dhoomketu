import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField



def main():
    pygame.init()
    print("Starting Asteroids!")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers=(updatable, drawable)
    
    player= Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        
        dt=clock.tick(60)/1000


    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    

if __name__ == "__main__":
    main()
