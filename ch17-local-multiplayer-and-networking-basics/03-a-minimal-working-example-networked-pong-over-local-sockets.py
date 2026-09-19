"""A minimal authoritative Pong server. Real production networking code
adds considerably more error handling, reconnection logic, and security
than this teaching example — treat this as a foundation to build on,
not a production-ready implementation."""
import json
import socket
import threading
import time

HOST, PORT = "0.0.0.0", 5555


class PongServerState:
    def __init__(self):
        self.left_paddle_y = 300.0
        self.right_paddle_y = 300.0
        self.ball_pos = [400.0, 300.0]
        self.ball_velocity = [220.0, 140.0]
        self.lock = threading.Lock()
        self._last_input_time = {"left": time.monotonic(), "right": time.monotonic()}

    def apply_input(self, player, direction):
        with self.lock:
            # Real delta time since this player's last input message,
            # not a fixed 1/60th assumption — matches Chapter 2's
            # delta-time principle even though input arrives at
            # whatever rate the client's network connection allows,
            # not a guaranteed fixed tick rate.
            now = time.monotonic()
            dt = now - self._last_input_time[player]
            self._last_input_time[player] = now
            speed = 260.0 * dt
            if player == "left":
                self.left_paddle_y += direction * speed
            else:
                self.right_paddle_y += direction * speed

    def step_physics(self, dt):
        with self.lock:
            self.ball_pos[0] += self.ball_velocity[0] * dt
            self.ball_pos[1] += self.ball_velocity[1] * dt
            if self.ball_pos[1] <= 0 or self.ball_pos[1] >= 600:
                self.ball_velocity[1] *= -1

    def snapshot(self):
        with self.lock:
            return {
                "left_paddle_y": self.left_paddle_y,
                "right_paddle_y": self.right_paddle_y,
                "ball_pos": list(self.ball_pos),
            }


def handle_client(conn, state, player):
    buffer = b""
    while True:
        try:
            data = conn.recv(1024)
        except OSError:
            break
        if not data:
            break
        buffer += data
        while b"\n" in buffer:
            line, buffer = buffer.split(b"\n", 1)
            try:
                message = json.loads(line.decode("utf-8"))
            except json.JSONDecodeError:
                continue
            if message.get("type") == "input":
                state.apply_input(player, message["direction"])


def broadcast_loop(state, connections):
    while True:
        state.step_physics(1 / 60)
        snapshot = json.dumps({"type": "state", **state.snapshot()}) + "\n"
        for conn in list(connections):
            try:
                conn.sendall(snapshot.encode("utf-8"))
            except OSError:
                connections.remove(conn)
        time.sleep(1 / 60)


def run_server():
    state = PongServerState()
    connections = []
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(2)
    print(f"Server listening on {HOST}:{PORT}")

    threading.Thread(target=broadcast_loop, args=(state, connections),
                     daemon=True).start()

    player_names = ["left", "right"]
    while len(connections) < 2:
        conn, addr = server_socket.accept()
        player = player_names[len(connections)]
        connections.append(conn)
        print(f"Player '{player}' connected from {addr}")
        threading.Thread(target=handle_client, args=(conn, state, player),
                         daemon=True).start()

    while True:
        time.sleep(1)


if __name__ == "__main__":
    run_server()
