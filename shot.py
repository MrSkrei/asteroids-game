import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS


class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity
        self.rect = pygame.Rect(
            x - SHOT_RADIUS, y - SHOT_RADIUS, SHOT_RADIUS * 2, SHOT_RADIUS * 2
        )
        if hasattr(self, "containers"):
            self.add(self.containers)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
