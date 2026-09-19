import pygame

TILE_SIZE = 40

PATH_TILES = [
    (0, 3), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1),
    (4, 1), (5, 1), (6, 1), (6, 2), (6, 3), (6, 4),
    (7, 4), (8, 4), (9, 4),
]

STARTING_GOLD = 150


class TowerMap:
    def __init__(self):
        self.path = PATH_TILES
        self.occupied = set()

    def can_place(self, tile):
        return tile not in self.path and tile not in self.occupied

    def place(self, tile):
        self.occupied.add(tile)

    def tile_center(self, tile):
        col, row = tile
        return (col * TILE_SIZE + TILE_SIZE // 2, row * TILE_SIZE + TILE_SIZE // 2)
