def run_editor(grid_width, grid_height, tile_definitions, save_dir):
    pygame.init()
    screen = pygame.display.set_mode((grid_width * CELL_SIZE + 160,
                                       grid_height * CELL_SIZE))
    pygame.display.set_caption("Level Editor")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 22)

    palette = TilePalette(tile_definitions)
    editor = TileEditor(grid_width, grid_height, palette)
    color_lookup = {key: color for key, color, _ in tile_definitions}

    running = True
    while running:
        dt = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    palette.select_next()
                elif event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    os.makedirs(save_dir, exist_ok=True)
                    editor.save(os.path.join(save_dir, "level.json"))
                    print("Saved.")

        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0]:  # left click: paint the selected tile
            mx, my = pygame.mouse.get_pos()
            if mx < grid_width * CELL_SIZE:
                col, row = mx // CELL_SIZE, my // CELL_SIZE
                editor.set_tile(col, row, palette.selected[0])
        elif mouse_buttons[2]:  # right click: erase to empty
            mx, my = pygame.mouse.get_pos()
            if mx < grid_width * CELL_SIZE:
                col, row = mx // CELL_SIZE, my // CELL_SIZE
                editor.set_tile(col, row, ".")

        screen.fill((15, 15, 20))
        for row in range(grid_height):
            for col in range(grid_width):
                key = editor.grid[row][col]
                color = color_lookup.get(key, (30, 30, 35))
                rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE,
                                   CELL_SIZE - 1, CELL_SIZE - 1)
                pygame.draw.rect(screen, color, rect)

        palette.draw(screen, (grid_width * CELL_SIZE + 15, 15))
        hint = font.render("Tab: cycle tile  L-click: paint  R-click: erase  Ctrl+S: save",
                           True, (200, 200, 200))
        screen.blit(hint, (10, grid_height * CELL_SIZE - 24))

        pygame.display.flip()

    pygame.quit()
