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

        # Position
        x = (screen.get_width() - surf.get_width()) // 2
        y = 275

        # --- Background rectangle ---
        padding = 10
        bg_rect = pygame.Rect(
            x - padding,
            y - padding,
            surf.get_width() + padding * 2,
            surf.get_height() + padding * 2
        )

        # Create transparent background surface
        bg_surf = pygame.Surface((bg_rect.width, bg_rect.height), pygame.SRCALPHA)
        bg_color = (170, 170, 170, int(self.alpha * 0.6))  # light gray, 60% of text alpha
        bg_surf.fill(bg_color)

        # Draw background then text
        screen.blit(bg_surf, (bg_rect.x, bg_rect.y))
        screen.blit(surf, (x, y))