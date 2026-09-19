import time

"""A minimal Pong client — sends input to the server, renders whatever
authoritative state the server most recently broadcast."""
import json
import socket
import threading

import pygame

SERVER_HOST, SERVER_PORT = "127.0.0.1", 5555


class NetworkClient:
    def __init__(self, player):
        self.player = player
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((SERVER_HOST, SERVER_PORT))
        self.latest_state = {"left_paddle_y": 300, "right_paddle_y": 300,
                             "ball_pos": [400, 300]}
        self.lock_thread = threading.Thread(target=self._listen, daemon=True)
        self.lock_thread.start()

    def _listen(self):
        buffer = b""
        while True:
            data = self.sock.recv(1024)
            if not data:
                break
            buffer += data
            while b"\n" in buffer:
                line, buffer = buffer.split(b"\n", 1)
                try:
                    message = json.loads(line.decode("utf-8"))
                except json.JSONDecodeError:
                    continue
                if message.get("type") == "state":
                    self.latest_state = message

    def send_input(self, direction):
        message = json.dumps({"type": "input", "direction": direction}) + "\n"
        try:
            self.sock.sendall(message.encode("utf-8"))
        except OSError:
            pass


def run_client(player):
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    client = NetworkClient(player)

    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        direction = 0
        if keys[pygame.K_UP]:
            direction = -1
        elif keys[pygame.K_DOWN]:
            direction = 1
        if direction != 0:
            client.send_input(direction)

        state = client.latest_state
        screen.fill((20, 20, 30))
        pygame.draw.rect(screen, (230, 230, 230),
                         (30, state["left_paddle_y"] - 45, 14, 90))
        pygame.draw.rect(screen, (230, 230, 230),
                         (756, state["right_paddle_y"] - 45, 14, 90))
        pygame.draw.circle(screen, (240, 200, 40), state["ball_pos"], 8)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    import sys
    run_client(sys.argv[1] if len(sys.argv) > 1 else "left")
