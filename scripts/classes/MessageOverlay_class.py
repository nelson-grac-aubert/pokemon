import pygame

class MessageOverlay:
    def __init__(self, font):
        self.font = font
        self.text = ""
        self.alpha = 0
        self.active = False
        self.fade_speed = 3  # Speed of fade-out
        self.duration = 60   # Frames before fade starts
        self.timer = 0

    def show(self, text):
        # Start displaying a new message
        self.text = text
        self.alpha = 255
        self.active = True
        self.timer = self.duration

    def update(self):
        if not self.active:
            return

        if self.timer > 0:
            self.timer -= 1
        else:
            self.alpha -= self.fade_speed
            if self.alpha <= 0:
                self.active = False

    def draw(self, screen):
        if not self.active:
            return

        # Render text
        surf = self.font.render(self.text, True, (255, 255, 255))
        surf.set_alpha(self.alpha)

        # Center on screen
        x = (screen.get_width() - surf.get_width()) // 2
        y = 275

        screen.blit(surf, (x, y))