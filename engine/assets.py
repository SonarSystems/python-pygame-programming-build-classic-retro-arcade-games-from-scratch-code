"""Loads and caches images and sounds so nothing is re-read from disk
mid-game. Every game in this book uses one shared AssetManager instance."""
import os

import pygame


class AssetManager:
    def __init__(self):
        self._images = {}
        self._sounds = {}

    def image(self, path):
        if path not in self._images:
            surface = pygame.image.load(path)
            self._images[path] = surface.convert_alpha()
        return self._images[path]

    def sound(self, path):
        if path not in self._sounds:
            self._sounds[path] = pygame.mixer.Sound(path)
        return self._sounds[path]

    def placeholder_image(self, size, color):
        """A solid-color Surface, for games that haven't added real art yet."""
        key = (size, color)
        if key not in self._images:
            surface = pygame.Surface(size, pygame.SRCALPHA)
            surface.fill(color)
            self._images[key] = surface
        return self._images[key]
