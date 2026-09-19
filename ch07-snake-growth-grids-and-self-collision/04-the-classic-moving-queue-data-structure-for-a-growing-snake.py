class Snake:
    def __init__(self, start_pos):
        self.body = [start_pos]
        self.direction = (1, 0)  # moving right
        self.grow_pending = 0

    def set_direction(self, new_direction):
        # Prevent reversing directly into yourself — moving right, then
        # immediately pressing left, would otherwise be an instant loss.
        opposite = (-new_direction[0], -new_direction[1])
        if opposite != self.direction:
            self.direction = new_direction

    def move(self):
        head_col, head_row = self.body[0]
        dir_col, dir_row = self.direction
        new_head = (head_col + dir_col, head_row + dir_row)
        self.body.insert(0, new_head)
        if self.grow_pending > 0:
            self.grow_pending -= 1
        else:
            self.body.pop()

    def grow(self, segments=1):
        self.grow_pending += segments

    @property
    def head(self):
        return self.body[0]
