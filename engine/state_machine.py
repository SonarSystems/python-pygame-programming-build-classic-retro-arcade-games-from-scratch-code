"""A simple named-state machine. Each state is identified by a string;
GameApp (below) uses this to decide which Scene is currently active."""


class StateMachine:
    def __init__(self, initial_state):
        self.state = initial_state
        self._listeners = []

    def on_change(self, callback):
        """Register a callback(old_state, new_state) fired on transition."""
        self._listeners.append(callback)

    def transition_to(self, new_state):
        old_state = self.state
        self.state = new_state
        for callback in self._listeners:
            callback(old_state, new_state)
