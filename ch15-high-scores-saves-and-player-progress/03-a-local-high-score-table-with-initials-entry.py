import pygame

class InitialsEntryScene(Scene):
    def __init__(self, app, score, high_scores):
        super().__init__()
        self.app = app
        self.score = score
        self.high_scores = high_scores
        self.letters = ["A", "A", "A"]
        self.cursor = 0
        self.font = pygame.font.Font(None, 56)

    def handle_event(self, event):
        if event.type != pygame.KEYDOWN:
            return
        if event.key == pygame.K_UP:
            self._cycle_letter(1)
        elif event.key == pygame.K_DOWN:
            self._cycle_letter(-1)
        elif event.key == pygame.K_RIGHT:
            self.cursor = min(2, self.cursor + 1)
        elif event.key == pygame.K_LEFT:
            self.cursor = max(0, self.cursor - 1)
        elif event.key == pygame.K_RETURN:
            initials = "".join(self.letters)
            self.high_scores.add_entry(initials, self.score)
            self.app.states.transition_to("menu")

    def _cycle_letter(self, direction):
        current = ord(self.letters[self.cursor]) - ord("A")
        current = (current + direction) % 26
        self.letters[self.cursor] = chr(ord("A") + current)
