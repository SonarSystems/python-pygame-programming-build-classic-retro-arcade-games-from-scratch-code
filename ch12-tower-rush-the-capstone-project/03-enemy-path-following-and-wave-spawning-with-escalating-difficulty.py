import pygame

class Enemy(Entity):
    def __init__(self, path, health, speed, reward, assets):
        self.path = path
        self.path_index = 0
        x, y = self._waypoint_pixels(self.path[0])
        image = assets.placeholder_image((22, 22), (200, 70, 70))
        super().__init__(image, x, y)
        self.speed = speed
        self.max_health = health
        self.health = health
        self.reward = reward

    def _waypoint_pixels(self, tile):
        col, row = tile
        return (col * TILE_SIZE + TILE_SIZE // 2, row * TILE_SIZE + TILE_SIZE // 2)

    def update(self, dt):
        if self.path_index >= len(self.path) - 1:
            return  # reached the end
        target = pygame.Vector2(self._waypoint_pixels(self.path[self.path_index + 1]))
        current = pygame.Vector2(self.rect.center)
        direction = target - current
        distance = direction.length()

        step = self.speed * dt
        if step >= distance:
            self.rect.center = target
            self.path_index += 1
        else:
            direction = direction.normalize()
            self.rect.center = current + direction * step

    def reached_end(self):
        return self.path_index >= len(self.path) - 1

    def take_damage(self, amount):
        self.health -= amount
        return self.health <= 0
