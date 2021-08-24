import pygame


class Tile:
    def __init__(self, value, row, column, width, height):
        self.value = value
        self.temp = 0
        self.row = row
        self.column = column
        self.width = width
        self.height = height
        self.highlighted = False

    def draw(self, window):
        font = pygame.font.SysFont('impact', 40)

        gap = self.width / 9
        x = self.column * gap
        y = self.row * gap

        if self.highlighted:
            pygame.draw.rect(window, (180, 180, 180), (x, y, gap, gap))

        if self.temp != 0 and self.value == 0:
            text = font.render(str(self.temp), True, (100, 100, 100))
            window.blit(text, (x + 5, y + 5))
        elif not self.value == 0:
            pygame.draw.rect(window, (0, 200, 0), (x, y, gap, gap))
            if self.highlighted:
                pygame.draw.rect(window, (180, 180, 180), (x, y, gap, gap))
            text = font.render(str(self.value), True, (0, 0, 0))
            window.blit(text, (x + (gap / 2 - text.get_width() / 2), y + (gap / 2 - text.get_height() / 2)))

    def set(self, value):
        self.value = value

    def set_temp(self, val):
        self.temp = val
