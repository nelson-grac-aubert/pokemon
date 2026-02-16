import pygame

class ConfirmationBox:
    def __init__(self, font):
        # Font used to render the dialog text
        self.font = font

        # Dialog state
        self.active = False      # True when the box is visible
        self.text = ""           # Text to display
        self.callback = None     # Function to call when box is dismissed

        # Box layout
        self.width = 500         # Box width
        self.height = 120        # Box height
        self.rect = None         # Will be centered later

    def show(self, screen_size, text, callback=None):
        # Activate the dialog with given text and optional callback
        self.active = True
        self.text = text
        self.callback = callback

        screen_w, screen_h = screen_size
        x = (screen_w - self.width) // 2
        y = (screen_h - self.height) // 2
        self.rect = pygame.Rect(x, y, self.width, self.height)

    def handle_click(self, pos):
        # Close the dialog on any click inside the box
        if not self.active:
            return

        if self.rect.collidepoint(pos):
            self.active = False
            if self.callback:
                self.callback()  # Call the continuation logic

    def draw(self, screen):
        # Draw the dialog box (assuming background already drawn)

        if not self.active:
            return

        # Grey overlay over the whole screen
        overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))  # Semi-transparent black
        screen.blit(overlay, (0, 0))

        # White box
        pygame.draw.rect(screen, (255, 255, 255), self.rect)

        # Simple black border
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 3)

        # Render text (single line for now)
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        text_x = self.rect.x + 20
        text_y = self.rect.y + (self.height - text_surface.get_height()) // 2
        screen.blit(text_surface, (text_x, text_y))