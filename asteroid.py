import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self,screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += dt * self.velocity

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            self.explosion_sound.play()
            return

        random_angle = random.uniform(20,50)

        velocity_1 = self.velocity.rotate( random_angle )
        velocity_2 = self.velocity.rotate( -random_angle )

        new_radii = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radii)
        new_asteroid1.velocity = velocity_1 * 1.2
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radii)
        new_asteroid2.velocity = velocity_2 * 1.2