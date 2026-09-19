def hyperspace_jump(ship):
    ship.rect.center = (random.randrange(800), random.randrange(600))
    ship.velocity = pygame.Vector2(0, 0)
