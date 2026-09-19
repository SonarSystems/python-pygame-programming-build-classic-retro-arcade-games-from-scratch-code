import pygame

def render_split_screen(main_surface, scene, camera_a, camera_b):
    half_width = main_surface.get_width() // 2
    height = main_surface.get_height()

    surface_a = pygame.Surface((half_width, height))
    surface_b = pygame.Surface((half_width, height))

    scene.draw_with_camera(surface_a, camera_a)
    scene.draw_with_camera(surface_b, camera_b)

    main_surface.blit(surface_a, (0, 0))
    main_surface.blit(surface_b, (half_width, 0))
    pygame.draw.line(main_surface, (10, 10, 10),
                     (half_width, 0), (half_width, height), 3)
