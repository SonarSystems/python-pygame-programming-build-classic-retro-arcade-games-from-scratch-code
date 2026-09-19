_image_cache = {}

def load_image(path):
    if path not in _image_cache:
        image = pygame.image.load(path).convert_alpha()
        _image_cache[path] = image
    return _image_cache[path]
