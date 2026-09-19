import pygame

all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()

bullet = Bullet(400, 300, -220, (240, 240, 240), assets)
all_sprites.add(bullet)
bullets.add(bullet)

# Later, once the bullet leaves the screen or hits something:
bullet.kill()  # removed from BOTH all_sprites and bullets automatically
