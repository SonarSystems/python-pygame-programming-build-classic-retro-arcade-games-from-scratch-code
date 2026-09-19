class Enemy(Entity):
    def __init__(self, path, health, speed, reward, assets,
                damage_type_resistances=None):
        # ... existing __init__ body ...
        # Defaulting to None/{} here, rather than a required positional
        # argument, means the existing build_wave call site below keeps
        # working unchanged for enemies that don't need resistances.
        self.resistances = damage_type_resistances or {}

    def take_damage(self, amount, damage_type="normal"):
        multiplier = 1.0 - self.resistances.get(damage_type, 0.0)
        self.health -= amount * multiplier
        return self.health <= 0
