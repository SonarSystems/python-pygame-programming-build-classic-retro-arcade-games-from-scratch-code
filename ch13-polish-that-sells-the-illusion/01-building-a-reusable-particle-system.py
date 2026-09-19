import random

import pygame


class Particle:
    def __init__(self, pos, velocity, color, lifetime, size=4):
        self.pos = pygame.Vector2(pos)
        self.velocity = pygame.Vector2(velocity)
        self.color = color
        self.lifetime = lifetime
        self.age = 0.0
        self.size = size

    def update(self, dt):
        self.pos += self.velocity * dt
        self.age += dt

    @property
    def alive(self):
        return self.age < self.lifetime

    @property
    def progress(self):
        return self.age / self.lifetime


class ParticleSystem:
    def __init__(self):
        self.particles = []

    def burst(self, pos, color, count=12, speed_range=(60, 220), lifetime=0.5):
        for _ in range(count):
            angle = random.uniform(0, 6.283)
            speed = random.uniform(*speed_range)
            velocity = pygame.Vector2(speed, 0).rotate_rad(angle)
            self.particles.append(Particle(pos, velocity, color, lifetime))

    def update(self, dt):
        for particle in self.particles:
            particle.update(dt)
        self.particles = [p for p in self.particles if p.alive]

    def draw(self, surface):
        for particle in self.particles:
            fade = 1.0 - particle.progress
            size = max(1, int(particle.size * fade))
            pygame.draw.circle(surface, particle.color,
                               (int(particle.pos.x), int(particle.pos.y)), size)
