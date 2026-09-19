def wrap_position(entity, width, height):
    if entity.rect.right < 0:
        entity.rect.left = width
    elif entity.rect.left > width:
        entity.rect.right = 0
    if entity.rect.bottom < 0:
        entity.rect.top = height
    elif entity.rect.top > height:
        entity.rect.bottom = 0
