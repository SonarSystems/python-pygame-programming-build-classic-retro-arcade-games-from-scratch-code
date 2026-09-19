def build_wave(wave_number, path, assets):
    count = 5 + wave_number * 2
    health = 30 + wave_number * 12
    speed = 60 + min(wave_number * 3, 40)
    reward = 8

    enemies = []
    for i in range(count):
        enemy = Enemy(path, health, speed, reward, assets)
        enemy.spawn_delay = i * 0.6  # stagger spawns so they don't overlap
        enemies.append(enemy)
    return enemies
