class OneWayPlatform(Entity):
    pass  # a plain solid rect; the special-case logic lives in collision resolution


def resolve_one_way_platforms(player, platforms, previous_bottom):
    for platform in platforms:
        if player.rect.colliderect(platform.rect) and player.velocity.y > 0:
            # Only block the player if they were above the platform's
            # top edge just before this frame's movement — otherwise a
            # player jumping up from underneath would get stuck.
            if previous_bottom <= platform.rect.top:
                player.rect.bottom = platform.rect.top
                player.velocity.y = 0
                player.on_ground = True
