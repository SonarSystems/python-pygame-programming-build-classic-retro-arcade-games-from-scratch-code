"""A general-purpose tile-based level editor. Run standalone; saves and
loads named level files as JSON, usable across any of this book's
tile-based games (Breakout's bricks, the platformer, Pac-Man's maze)."""
import json
import os

import pygame

CELL_SIZE = 32


class TilePalette:
    def __init__(self, tile_definitions):
        # tile_definitions: list of (key, display_color, label) tuples
        self.tiles = tile_definitions
        self.selected_index = 0

    def select_next(self):
        self.selected_index = (self.selected_index + 1) % len(self.tiles)

    def select_previous(self):
        self.selected_index = (self.selected_index - 1) % len(self.tiles)

    @property
    def selected(self):
        return self.tiles[self.selected_index]

    def draw(self, surface, position):
        x, y = position
        for i, (key, color, label) in enumerate(self.tiles):
            rect = pygame.Rect(x, y + i * 36, 30, 30)
            pygame.draw.rect(surface, color, rect)
            if i == self.selected_index:
                pygame.draw.rect(surface, (255, 255, 255), rect, width=2)


class TileEditor:
    def __init__(self, grid_width, grid_height, palette):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.palette = palette
        self.grid = [["." for _ in range(grid_width)] for _ in range(grid_height)]

    def set_tile(self, col, row, key):
        if 0 <= row < self.grid_height and 0 <= col < self.grid_width:
            self.grid[row][col] = key

    def to_rows(self):
        return ["".join(row) for row in self.grid]

    def save(self, path, metadata=None):
        payload = {"rows": self.to_rows(), "metadata": metadata or {}}
        with open(path, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2)

    def load(self, path):
        with open(path, "r", encoding="utf-8") as f:
            payload = json.load(f)
        rows = payload["rows"]
        self.grid_height = len(rows)
        self.grid_width = max(len(row) for row in rows)
        self.grid = [list(row.ljust(self.grid_width, ".")) for row in rows]
        return payload.get("metadata", {})
