from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt: float):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            new_dir = random.uniform(20, 50)
            rad = self.radius - ASTEROID_MIN_RADIUS
            ast1 = Asteroid(self.position.x, self.position.y, rad)
            ast2 = Asteroid(self.position.x, self.position.y, rad)
            speed = self.velocity * 1.2
            dir1 = self.velocity.rotate(new_dir)
            dir2 = self.velocity.rotate(-new_dir)
            ast1.velocity = dir1
            ast2.velocity = dir2