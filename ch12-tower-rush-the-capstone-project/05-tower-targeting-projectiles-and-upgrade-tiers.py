import pygame

class Tower(Entity):
    def __init__(self, x, y, tower_range, damage, fire_rate, assets):
        image = assets.placeholder_image((30, 30), (80, 160, 220))
        super().__init__(image, x, y)
        self.range = tower_range
        self.damage = damage
        self.fire_cooldown = 0.0
        self.fire_rate = fire_rate  # seconds between shots
        self.level = 1

    def find_target(self, enemies):
        my_pos = pygame.Vector2(self.rect.center)
        in_range = [e for e in enemies
                    if my_pos.distance_to(e.rect.center) <= self.range]
        if not in_range:
            return None
        # Prioritize whichever enemy is furthest along the path — this
        # protects the end of the path first, which is usually the
        # correct priority in a tower-defense game.
        return max(in_range, key=lambda e: e.path_index)

    def update(self, dt, enemies, projectiles, assets):
        self.fire_cooldown = max(0.0, self.fire_cooldown - dt)
        if self.fire_cooldown <= 0:
            target = self.find_target(enemies)
            if target is not None:
                self.fire_cooldown = self.fire_rate
                projectiles.append(Projectile(self.rect.center, target, self.damage, assets))

    def upgrade(self):
        self.level += 1
        self.damage = int(self.damage * 1.5)
        self.range += 12
        self.fire_rate = max(0.15, self.fire_rate * 0.88)


class Projectile:
    def __init__(self, start_pos, target, damage, assets):
        self.pos = pygame.Vector2(start_pos)
        self.target = target
        self.damage = damage
        self.speed = 420.0
        self.assets = assets

    def update(self, dt):
        if self.target.health <= 0:
            return "expired"
        direction = pygame.Vector2(self.target.rect.center) - self.pos
        distance = direction.length()
        step = self.speed * dt
        if step >= distance:
            self.target.take_damage(self.damage)
            return "hit"
        self.pos += direction.normalize() * step
        return "flying"
