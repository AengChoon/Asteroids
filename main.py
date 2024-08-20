import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot

def main():
    pygame.init()

    clock = pygame.time.Clock()
    delta_time = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    my_player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)
    my_asteroidfield = AsteroidField()

    Shot.containers = (shots, updatable, drawable)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for instance in updatable:
            instance.update(delta_time)

        for instance in asteroids:
            if instance.is_colliding(my_player):
                print("Game over!")
                return

        for instance in drawable:
            instance.draw(screen)

        pygame.display.flip()
        delta_time = clock.tick(60) / 1000


if __name__ == "__main__":
    main()