import pygame

class DialogBox:

    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.message = None

        # Dialog box size
        self.width = 500
        self.height = 120

    def show(self, message: str):
        """Display a dialog message."""
        self.message = message

    def hide(self):
        """Close the dialog."""
        self.message = None

    def is_open(self):
        return self.message is not None

    def handle_event(self, event):
        """Close the dialog on any click."""
        if self.message and event.type == pygame.MOUSEBUTTONDOWN:
            self.hide()

    def draw(self):
        if not self.message:
            return

        w, h = self.width, self.height
        x = (self.screen.get_width() - w) // 2
        y = 100
        rect = pygame.Rect(x, y, w, h)

        # Background
        pygame.draw.rect(self.screen, (255, 255, 255), rect)
        pygame.draw.rect(self.screen, (0, 0, 0), rect, 4)

        # Word wrap
        max_width = w - 40
        words = self.message.split(" ")
        lines = []
        current = ""

        for word in words:
            test = current + word + " "
            if self.font.size(test)[0] <= max_width:
                current = test
            else:
                lines.append(current)
                current = word + " "
        lines.append(current)

        rendered_lines = [self.font.render(line, True, (0, 0, 0)) for line in lines]
        total_height = sum(surface.get_height() for surface in rendered_lines)
        start_y = rect.centery - total_height // 2

        current_y = start_y
        for surface in rendered_lines:
            text_rect = surface.get_rect(center=(rect.centerx, current_y + surface.get_height() // 2))
            self.screen.blit(surface, text_rect)
            current_y += surface.get_height()