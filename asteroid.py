import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        pygame.sprite.Sprite.__init__(self, self.containers)
        super().__init__(x, y, radius)
        self.velocity = pygame.math.Vector2(0, 0)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        groups = self.groups()
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)

        new_velocity1 = pygame.math.Vector2(self.velocity).rotate(random_angle)
        new_velocity2 = pygame.math.Vector2(self.velocity).rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid1 = Asteroid(
            x=self.position.x,
            y=self.position.y,
            radius=new_radius,
        )
        new_asteroid1.velocity = new_velocity1 * 1.2
        for group in groups:
            group.add(new_asteroid1)

        new_asteroid2 = Asteroid(
            x=self.position.x,
            y=self.position.y,
            radius=new_radius,
        )
        new_asteroid2.velocity = new_velocity2 * 1.2
        for group in groups:
            group.add(new_asteroid2)
