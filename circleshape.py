import pygame


class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):

        if hasattr(self, "containers"):
            super().__init__()
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        WHITE = (255, 255, 255)
        pygame.draw.polygon(screen, WHITE, self.triangle(), 2)

    def update(self, dt):
        # sub-classes must override
        pass

    def collision(self, other):
        distance = self.position.distance_to(other.position)
        return distance <= (self.radius + other.radius)
