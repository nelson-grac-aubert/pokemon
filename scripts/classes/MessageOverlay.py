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

        # Split lines
        lines = self.text.split("\n")

        # Render all lines
        rendered = [self.font.render(line, True, (255, 255, 255)) for line in lines]

        # Compute total height
        total_height = sum(s.get_height() for s in rendered) + (len(lines) - 1) * 5

        # Position
        x = (screen.get_width() - max(s.get_width() for s in rendered)) // 2
        y = 100

        # Background rectangle
        padding = 10
        bg_rect = pygame.Rect(
            x - padding,
            y - padding,
            max(s.get_width() for s in rendered) + padding * 2,
            total_height + padding * 2
        )

        # Background surface
        bg_surf = pygame.Surface((bg_rect.width, bg_rect.height), pygame.SRCALPHA)
        bg_color = (170, 170, 170, int(self.alpha * 0.6))
        bg_surf.fill(bg_color)

        # Draw background
        screen.blit(bg_surf, (bg_rect.x, bg_rect.y))

        # Draw each line with spacing
        current_y = y
        for surf in rendered:
            surf.set_alpha(self.alpha)
            screen.blit(surf, (x, current_y))
            current_y += surf.get_height() + 5
