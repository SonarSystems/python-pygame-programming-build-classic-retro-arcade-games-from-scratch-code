pygame.mixer.init()
hit_sound = pygame.mixer.Sound("assets/sounds/hit.wav")

# anywhere in your update logic:
hit_sound.play()
