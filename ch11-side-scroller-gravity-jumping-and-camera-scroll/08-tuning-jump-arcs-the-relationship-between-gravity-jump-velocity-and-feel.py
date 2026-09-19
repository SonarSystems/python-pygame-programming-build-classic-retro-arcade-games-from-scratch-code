def jump_stats(jump_velocity, gravity):
    peak_height = (jump_velocity ** 2) / (2 * gravity)
    airtime = (2 * abs(jump_velocity)) / gravity
    return peak_height, airtime

# With this chapter's values: JUMP_VELOCITY = -560, GRAVITY = 1450
height, airtime = jump_stats(560, 1450)
print(f"Peak height: {height:.0f}px, Airtime: {airtime:.2f}s")
# Peak height: 108px, Airtime: 0.77s
