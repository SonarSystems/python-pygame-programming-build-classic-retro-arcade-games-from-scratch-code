import pygame

pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i)
             for i in range(pygame.joystick.get_count())]
for joystick in joysticks:
    joystick.init()

# inside update, if at least one joystick is connected:
if joysticks:
    axis_x = joysticks[0].get_axis(0)  # -1.0 (left) to 1.0 (right)
    if abs(axis_x) > 0.2:  # dead zone, avoids drift from an uncentered stick
        paddle.velocity.x = axis_x * PADDLE_SPEED
