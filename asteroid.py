from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x_pos = x
        self.y_pos = y

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if (self.radius <= ASTEROID_MIN_RADIUS):
            return
        
        random_angle = random.uniform(20, 50)
        neg_rand_ang = random_angle - random_angle - random_angle
        vect1 = self.velocity.rotate(random_angle)
        vect2 = self.velocity.rotate(neg_rand_ang)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        ast1 = Asteroid(self.position.x, self.position.y, new_radius)
        #ast1.position = self.position
        ast1.velocity = vect1 * 1.2

        ast2 = Asteroid(self.position.x, self.position.y, new_radius)
        #ast2.position = self.position
        ast2.velocity = vect2 * 1.2
            

    #def check_collision(self, circle_shape):
        #super().check_collision(circle_shape)