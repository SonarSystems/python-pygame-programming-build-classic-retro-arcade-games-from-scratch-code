import pygame

def check_checkpoints(player, checkpoints, level_state):
    for checkpoint in checkpoints:
        if player.rect.colliderect(checkpoint.rect) and not checkpoint.activated:
            checkpoint.activated = True
            level_state.respawn_point = checkpoint.rect.center


def respawn_player(player, level_state):
    player.rect.center = level_state.respawn_point
    player.velocity = pygame.Vector2(0, 0)
