def build_cannon_tower(x, y, assets):
    return Tower(x, y, tower_range=90, damage=18, fire_rate=1.1, assets=assets)

def build_rapid_tower(x, y, assets):
    return Tower(x, y, tower_range=70, damage=4, fire_rate=0.15, assets=assets)
