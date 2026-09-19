import pygame

keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT]:
    paddle.velocity.x = -PADDLE_SPEED
elif keys[pygame.K_RIGHT]:
    paddle.velocity.x = PADDLE_SPEED
else:
    paddle.velocity.x = 0
