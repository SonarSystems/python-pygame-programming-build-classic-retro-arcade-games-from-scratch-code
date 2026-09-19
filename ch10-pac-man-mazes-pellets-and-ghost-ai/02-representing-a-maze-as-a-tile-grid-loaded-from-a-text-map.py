class Maze:
    def __init__(self, rows):
        self.rows = rows
        self.width = max(len(row) for row in rows)
        self.height = len(rows)
        self.pellets = set()
        self.power_pellets = set()
        for row_index, row in enumerate(rows):
            for col_index, char in enumerate(row):
                if char == ".":
                    self.pellets.add((col_index, row_index))
                elif char == "o":
                    self.power_pellets.add((col_index, row_index))

    def is_wall(self, col, row):
        if row < 0 or row >= self.height or col < 0 or col >= self.width:
            return True
        return self.rows[row][col] == "#"

    def tile_center_pixels(self, col, row):
        return (col * TILE_SIZE + TILE_SIZE // 2, row * TILE_SIZE + TILE_SIZE // 2)
