import pygame
from circleshape import CircleShape
import constants
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.position = pygame.Vector2(x, y)
        self.rotation = 0
        self.cooldown = 0

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, delta_time):
        self.rotation += constants.PLAYER_TURN_SPEED * delta_time

    def move(self, delta_time):
        forward = pygame.Vector2(0, 1)
        direction = forward.rotate(self.rotation)
        self.position += direction * constants.PLAYER_SPEED * delta_time

    def shoot(self):
        if self.cooldown > 0:
            return

        self.cooldown = constants.PLAYER_SHOOT_COOLDOWN
        new_shot = Shot(self.position.x, self.position.y)
        new_shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * constants.PLAYER_SHOOT_SPEED

    def update(self, delta_time):
        self.cooldown -= delta_time
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-delta_time)
        if keys[pygame.K_d]:
            self.rotate(delta_time)
        if keys[pygame.K_w]:
            self.move(delta_time)
        if keys[pygame.K_s]:
            self.move(-delta_time)
        if keys[pygame.K_SPACE]:
            self.shoot()