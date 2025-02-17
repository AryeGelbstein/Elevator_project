from constants import *


class Floor:

    def __init__(self, num):
        self.num = num
        self.button_center = None
        self.button_pressed = False
        self.font_color = BLACK if not self.button_pressed else GREEN



    def is_button_pressed(self, x, y):
        cx, cy = self.button_center
        if ((cx - x) ** 2 + (cy - y) ** 2) ** 0.5 <= BUTTON_RADIUS:
            self.button_pressed = True
            return self.num
        return None


    def draw_button_with_numbers(self, screen, center):
        pygame.draw.circle(screen, BUTTON_COLOR, center, BUTTON_RADIUS)
        font = pygame.font.Font(None, FONT_SIZE)
        font_color = BLACK if not self.button_pressed else GREEN
        outline_color = font_color
        text = font.render(f'{self.num +1}', True, font_color)
        text_rect = text.get_rect(center = center)
        screen.blit(text, text_rect)
        pygame.draw.circle(screen, outline_color, center, BUTTON_RADIUS, width=1)


    def draw_timer(self, screen, center):
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time -



    def draw(self, image, screen, spacer_color=BLACK):
        top_left = (MARGIN, screen.get_height() - MARGIN - FLOOR_HEIGHT * (self.num + 1))
        screen.blit(image, top_left)
        x, y = top_left
        rect = pygame.Rect(x, y, FLOOR_WIDTH, FLOOR_SPACER_HEIGHT)
        pygame.draw.rect(screen, spacer_color, rect)
        center = x + FLOOR_WIDTH // 2, y + FLOOR_HEIGHT // 2 + FLOOR_SPACER_HEIGHT // 2
        x, y = center
        self.button_center = x, y - screen.get_height() + WINDOW_HEIGHT
        self.draw_button_with_numbers(screen, center)
#           self.draw_timer(screen, FLOOR_WIDTH, y)


