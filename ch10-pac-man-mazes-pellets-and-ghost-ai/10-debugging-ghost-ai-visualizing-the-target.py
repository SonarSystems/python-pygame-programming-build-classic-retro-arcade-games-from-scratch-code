import pygame

def draw_debug_targets(ghosts, maze, surface, pacman):
    for ghost in ghosts:
        target = ghost._current_target(pacman)
        tx, ty = maze.tile_center_pixels(*target)
        pygame.draw.circle(surface, ghost.base_color, (tx, ty), 4, width=1)
