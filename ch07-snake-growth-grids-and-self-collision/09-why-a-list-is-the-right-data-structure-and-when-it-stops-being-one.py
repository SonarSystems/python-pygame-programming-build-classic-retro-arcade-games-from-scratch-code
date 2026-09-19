from collections import deque

class Snake:
    def __init__(self, start_pos):
        self.body = deque([start_pos])
        # ... rest of __init__ unchanged ...

    def move(self):
        head_col, head_row = self.body[0]
        dir_col, dir_row = self.direction
        new_head = (head_col + dir_col, head_row + dir_row)
        self.body.appendleft(new_head)
        if self.grow_pending > 0:
            self.grow_pending -= 1
        else:
            self.body.pop()
