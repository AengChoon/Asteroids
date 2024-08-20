import random

import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            first_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            first_velocity = self.velocity.rotate(random_angle)
            first_asteroid.velocity = first_velocity * 1.2

            second_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            second_velocity = self.velocity.rotate(-random_angle)
            second_asteroid.velocity = second_velocity * 1.2

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, delta_time):
        self.position += self.velocity * delta_time