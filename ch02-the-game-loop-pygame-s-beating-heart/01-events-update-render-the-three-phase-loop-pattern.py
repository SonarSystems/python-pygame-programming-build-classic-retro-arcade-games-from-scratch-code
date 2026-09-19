import pygame

running = True
while running:
    # 1. Process input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. Update
    # (nothing to update yet — the window is static)

    # 3. Render
    screen.fill((20, 20, 30))
    pygame.display.flip()

    clock.tick(60)
