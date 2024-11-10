import pygame
from constants import PLAYER_RADIUS
from circleshape import CircleShape
from constants import PLAYER_TURN_SPEED
from constants import PLAYER_SPEED
from constants import PLAYER_SHOOT_SPEED
from constants import PLAYER_SHOOT_COOLDOWN
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y, shots_group):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shots = shots_group
        self.cooldown_timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def shoot(self):
        if self.cooldown_timer > 0:
            pass
        else:
            initial_velocity = pygame.Vector2(0, 1)
            initial_velocity = initial_velocity.rotate(self.rotation)
            initial_velocity *= PLAYER_SHOOT_SPEED
            shot = Shot(self.position.x, self.position.y, initial_velocity)
            self.shots.add(shot)
            self.cooldown_timer = PLAYER_SHOOT_COOLDOWN

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE] and not self.space_pressed:
            self.shoot()
        self.space_pressed = keys[pygame.K_SPACE]
        if self.cooldown_timer > 0:
            self.cooldown_timer -= dt
            if self.cooldown_timer < 0:
                self.cooldown_timer = 0

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
