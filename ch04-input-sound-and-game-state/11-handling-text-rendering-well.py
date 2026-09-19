text_surface = self.font.render(message, True, (240, 240, 240))
text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
surface.blit(text_surface, text_rect)
