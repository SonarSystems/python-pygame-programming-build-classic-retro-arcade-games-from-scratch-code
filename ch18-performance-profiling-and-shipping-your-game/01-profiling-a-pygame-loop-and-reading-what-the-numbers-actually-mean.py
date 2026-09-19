import cProfile
import pstats

def run_profiled():
    from engine.game_loop import GameLoop
    loop = GameLoop(800, 600, "Profiled Run")
    # ... set up the scene you want to profile ...
    loop.run()

profiler = cProfile.Profile()
profiler.enable()
run_profiled()  # play for a representative amount of time, then close the window
profiler.disable()

stats = pstats.Stats(profiler)
stats.sort_stats("cumulative")
stats.print_stats(20)  # top 20 functions by total time spent
