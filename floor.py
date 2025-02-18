from constants import *


class Floor:

    def __init__(self, num):
        # Initializes a floor object.
        # Each floor has a number, a button state, and a button position for user interaction.

        self.num = num
        self.button_center = None
        self.button_pressed = False
        self.font_color = BLACK if not self.button_pressed else GREEN



    def is_button_pressed(self, x, y):
        # Checks if the floor button was pressed.
        # If the button is within the click radius, it is marked as pressed and the floor number is returned.

        cx, cy = self.button_center
        if ((cx - x) ** 2 + (cy - y) ** 2) ** 0.5 <= BUTTON_RADIUS:
            self.button_pressed = True
            return self.num
        return None


    def draw_button_with_numbers(self, screen, center):
        # Draws a circular button for the floor with a number inside.
        # The button color changes if it is pressed, and an outline is drawn around it.

        pygame.draw.circle(screen, BUTTON_COLOR, center, BUTTON_RADIUS)
        font = pygame.font.Font(None, FONT_SIZE)
        font_color = BLACK if not self.button_pressed else GREEN
        outline_color = font_color
        text = font.render(f'{self.num +1}', True, font_color)
        text_rect = text.get_rect(center = center)
        screen.blit(text, text_rect)
        pygame.draw.circle(screen, outline_color, center, BUTTON_RADIUS, width=1)



    def draw(self, image, screen, spacer_color=BLACK):
        # Draws the floor on the screen, including the floor image and spacer.
        # Positions the floor button correctly and calls the function to draw it.

        top_left = (MARGIN, screen.get_height() - MARGIN - FLOOR_HEIGHT * (self.num + 1))
        screen.blit(image, top_left)
        x, y = top_left
        rect = pygame.Rect(x, y, FLOOR_WIDTH, FLOOR_SPACER_HEIGHT)
        pygame.draw.rect(screen, spacer_color, rect)
        center = x + FLOOR_WIDTH // 2, y + FLOOR_HEIGHT // 2 + FLOOR_SPACER_HEIGHT // 2
        x, y = center
        self.button_center = x, y - screen.get_height() + WINDOW_HEIGHT
        self.draw_button_with_numbers(screen, center)



