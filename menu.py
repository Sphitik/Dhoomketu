import pygame

class Menu:
    def __init__(self, screen, title, options):
        self.screen = screen
        self.title = title
        self.options = options
        self.font = pygame.font.Font(None, 74)
        self.option_font = pygame.font.Font(None, 50)
        self.selected_option = 0

    def draw(self):
        self.screen.fill("black")
        title_text = self.font.render(self.title, True, "white")
        title_rect = title_text.get_rect(center=(self.screen.get_width() / 2, self.screen.get_height() / 4))
        self.screen.blit(title_text, title_rect)

        for i, option in enumerate(self.options):
            color = "yellow" if i == self.selected_option else "white"
            option_text = self.option_font.render(option, True, color)
            option_rect = option_text.get_rect(center=(self.screen.get_width() / 2, self.screen.get_height() / 2 + i * 60))
            self.screen.blit(option_text, option_rect)

        pygame.display.flip()

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.selected_option = (self.selected_option - 1) % len(self.options)
            elif event.key == pygame.K_s:
                self.selected_option = (self.selected_option + 1) % len(self.options)
            elif event.key == pygame.K_RETURN:
                return self.options[self.selected_option]
        return None
