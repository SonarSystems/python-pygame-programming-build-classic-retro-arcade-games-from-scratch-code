# Python Pygame Programming — Companion Code

*Build Classic Retro Arcade Games from Scratch*

This is the official companion code repository for **Python Pygame Programming**, published by SonarSystems. Every runnable example in the book lives here, organized by chapter, exactly as it appears in the text — clone it, follow along, and run the examples yourself instead of retyping them from the page.

## Chapters

| Chapter | Title | Code |
|---|---|---|
| 1 | Setting Up Your Arcade Workshop | [`ch01-setting-up-your-arcade-workshop/`](ch01-setting-up-your-arcade-workshop/) — 3 files |
| 2 | The Game Loop — Pygame's Beating Heart | [`ch02-the-game-loop-pygame-s-beating-heart/`](ch02-the-game-loop-pygame-s-beating-heart/) — 6 files |
| 3 | Drawing, Moving, and Colliding | [`ch03-drawing-moving-and-colliding/`](ch03-drawing-moving-and-colliding/) — 16 files |
| 4 | Input, Sound, and Game State | [`ch04-input-sound-and-game-state/`](ch04-input-sound-and-game-state/) — 14 files |
| 5 | Pong — Where the Arcade Began | [`ch05-pong-where-the-arcade-began/`](ch05-pong-where-the-arcade-began/) — 8 files |
| 6 | Breakout — Bricks, Bounces, and Levels | [`ch06-breakout-bricks-bounces-and-levels/`](ch06-breakout-bricks-bounces-and-levels/) — 14 files |
| 7 | Snake — Growth, Grids, and Self-Collision | [`ch07-snake-growth-grids-and-self-collision/`](ch07-snake-growth-grids-and-self-collision/) — 11 files |
| 8 | Space Invaders — Waves, Formations, and Escalation | [`ch08-space-invaders-waves-formations-and-escalation/`](ch08-space-invaders-waves-formations-and-escalation/) — 10 files |
| 9 | Asteroids — Momentum, Wraparound, and Vector Movement | [`ch09-asteroids-momentum-wraparound-and-vector-movement/`](ch09-asteroids-momentum-wraparound-and-vector-movement/) — 8 files |
| 10 | Pac-Man — Mazes, Pellets, and Ghost AI | [`ch10-pac-man-mazes-pellets-and-ghost-ai/`](ch10-pac-man-mazes-pellets-and-ghost-ai/) — 10 files |
| 11 | Side-Scroller — Gravity, Jumping, and Camera Scroll | [`ch11-side-scroller-gravity-jumping-and-camera-scroll/`](ch11-side-scroller-gravity-jumping-and-camera-scroll/) — 9 files |
| 12 | Tower Rush — The Capstone Project | [`ch12-tower-rush-the-capstone-project/`](ch12-tower-rush-the-capstone-project/) — 9 files |
| 13 | Polish That Sells the Illusion | [`ch13-polish-that-sells-the-illusion/`](ch13-polish-that-sells-the-illusion/) — 6 files |
| 14 | Sound Design and Music on a Budget | [`ch14-sound-design-and-music-on-a-budget/`](ch14-sound-design-and-music-on-a-budget/) — 8 files |
| 15 | High Scores, Saves, and Player Progress | [`ch15-high-scores-saves-and-player-progress/`](ch15-high-scores-saves-and-player-progress/) — 9 files |
| 16 | Content Pipelines and Level Tools | [`ch16-content-pipelines-and-level-tools/`](ch16-content-pipelines-and-level-tools/) — 6 files |
| 17 | Local Multiplayer and Networking Basics | [`ch17-local-multiplayer-and-networking-basics/`](ch17-local-multiplayer-and-networking-basics/) — 4 files |
| 18 | Performance, Profiling, and Shipping Your Game | [`ch18-performance-profiling-and-shipping-your-game/`](ch18-performance-profiling-and-shipping-your-game/) — 6 files |
| 19 | Packaging and Distributing Your Arcade Collection | [`ch19-packaging-and-distributing-your-arcade-collection/`](ch19-packaging-and-distributing-your-arcade-collection/) — 2 files |

## The `engine/` package

Several early chapters build up a small, reusable engine — classes shared across every later chapter's examples rather than redefined each time. This repo assembles those classes into a real, importable `engine/` package at the repo root (mirroring the project layout the book itself has you build), so `from engine.game_loop import GameLoop`-style imports in later chapters resolve exactly like they do if you followed along and built the same structure yourself. Run any example that imports from `engine/` from the repo root (or add the repo root to your `PYTHONPATH`) for the import to work:

```bash
cd python-pygame-programming-build-classic-retro-arcade-games-from-scratch-code
python3 chNN-.../NN-example.py
```

## Prerequisites

- **Json**
- **Python** — Python 3.10+.

## Running the examples

**Python** — run a single example directly:

```bash
python3 chNN-.../NN-example.py
```

## Running the tests

Every example has a smoke test under `tests/` (compiles cleanly for compiled languages; runs cleanly and passes its assertions for scripted languages). From the repo root:

```bash
pip3 install pytest
pytest tests/ -v
```

## License

The code in this repository is released under the MIT License — see [`LICENSE`](LICENSE). The accompanying book text is a separate, commercial work and is **not** covered by this license.

---

This is the official companion repository for *Python Pygame Programming* (github.com/SonarSystems/python-pygame-programming-build-classic-retro-arcade-games-from-scratch-code), maintained by SonarSystems.
