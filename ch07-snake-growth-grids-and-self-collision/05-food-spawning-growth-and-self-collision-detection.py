import random


def spawn_food(snake_body):
    while True:
        pos = (random.randrange(GRID_WIDTH), random.randrange(GRID_HEIGHT))
        if pos not in snake_body:
            return pos
