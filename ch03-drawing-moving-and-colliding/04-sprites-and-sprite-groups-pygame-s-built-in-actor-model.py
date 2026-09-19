all_sprites = pygame.sprite.Group()
ball = Ball(400, 300)
all_sprites.add(ball)

# inside the game loop's update phase:
all_sprites.update(dt)

# inside the game loop's render phase:
all_sprites.draw(screen)
