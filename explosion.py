import pygame
import random
from constants import *
from circleshape import CircleShape

class Explosion(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, EXPLOSION_RADIUS)
        self.timer = 0.5

    def draw(self, screen):
        points = []
        for angle in range(0, 360, 60):
            dist = self.radius + random.uniform(-10, 10)
            point = self.position + pygame.Vector2(dist, 0).rotate(angle)
            points.append(point)
        pygame.draw.polygon(screen, (255, 0, 0), points, 2)

    def update(self, dt):
        self.timer -= dt
        self.radius += 20 * dt
        if self.timer <= 0:
            self.kill()
