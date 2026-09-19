BASE_TICK_INTERVAL = 0.13
MIN_TICK_INTERVAL = 0.055
TICK_DECREASE_PER_FOOD = 0.003

def current_tick_interval(score):
    foods_eaten = score // 10
    interval = BASE_TICK_INTERVAL - (foods_eaten * TICK_DECREASE_PER_FOOD)
    return max(MIN_TICK_INTERVAL, interval)
