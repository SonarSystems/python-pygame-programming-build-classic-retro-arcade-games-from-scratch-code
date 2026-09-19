"""Run this, click grid cells to cycle through brick colors, press S to
print the resulting level as a Python string list to the terminal."""
import pygame

CELL = 40
COLORS = [".", "R", "O", "Y", "G"]
COLOR_MAP = {".": (10, 10, 10), "R": (220, 70, 60), "O": (230, 140, 40),
             "Y": (230, 200, 40), "G": (90, 200, 90)}

pygame.init()
grid = [["." for _ in range(12)] for _ in range(6)]
screen = pygame.display.set_mode((12 * CELL, 6 * CELL))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            col, row = event.pos[0] // CELL, event.pos[1] // CELL
            current = COLORS.index(grid[row][col])
            grid[row][col] = COLORS[(current + 1) % len(COLORS)]
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            for row in grid:
                print('"' + "".join(row) + '",')
    for row_index, row in enumerate(grid):
        for col_index, char in enumerate(row):
            rect = pygame.Rect(col_index * CELL, row_index * CELL, CELL - 2, CELL - 2)
            pygame.draw.rect(screen, COLOR_MAP[char], rect)
    pygame.display.flip()
pygame.quit()
