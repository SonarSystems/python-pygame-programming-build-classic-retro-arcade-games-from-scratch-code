CELL_SIZE = 64


class SpatialGrid:
    def __init__(self):
        self.cells = {}

    def clear(self):
        self.cells.clear()

    def insert(self, entity):
        cell = (entity.rect.centerx // CELL_SIZE, entity.rect.centery // CELL_SIZE)
        self.cells.setdefault(cell, []).append(entity)

    def nearby(self, entity):
        cx, cy = entity.rect.centerx // CELL_SIZE, entity.rect.centery // CELL_SIZE
        result = []
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                result.extend(self.cells.get((cx + dx, cy + dy), []))
        return result
