import pygame

SHIELD_BLOCK_SIZE = 4


class ShieldBlock(Entity):
    def __init__(self, x, y, assets):
        image = assets.placeholder_image((SHIELD_BLOCK_SIZE, SHIELD_BLOCK_SIZE),
                                          (90, 200, 90))
        super().__init__(image, x, y)


def build_shield(x, y, assets):
    blocks = pygame.sprite.Group()
    # A simple bunker silhouette: a solid rectangle with a notch cut from
    # the bottom-center, matching the classic shield shape.
    rows, cols = 12, 16
    for row in range(rows):
        for col in range(cols):
            if row >= rows - 4 and cols // 2 - 3 <= col <= cols // 2 + 2:
                continue  # the notch
            block_x = x + col * SHIELD_BLOCK_SIZE
            block_y = y + row * SHIELD_BLOCK_SIZE
            blocks.add(ShieldBlock(block_x, block_y, assets))
    return blocks
