"""A minimal test for StateMachine, using Python's built-in unittest —
no Pygame window or event loop required, since StateMachine has no
dependency on either."""
import unittest

from engine.state_machine import StateMachine


class TestStateMachine(unittest.TestCase):
    def test_initial_state(self):
        machine = StateMachine("menu")
        self.assertEqual(machine.state, "menu")

    def test_transition_changes_state(self):
        machine = StateMachine("menu")
        machine.transition_to("playing")
        self.assertEqual(machine.state, "playing")

    def test_on_change_fires_with_correct_args(self):
        machine = StateMachine("menu")
        received = []
        machine.on_change(lambda old, new: received.append((old, new)))
        machine.transition_to("playing")
        self.assertEqual(received, [("menu", "playing")])


if __name__ == "__main__":
    unittest.main()
