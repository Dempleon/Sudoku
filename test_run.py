import pygame
from pygame.locals import *

board = [[7, 8, 0, 4, 0, 0, 1, 2, 0],
         [6, 0, 0, 0, 7, 5, 0, 0, 9],
         [0, 0, 0, 6, 0, 1, 0, 7, 8],
         [0, 0, 7, 0, 4, 0, 2, 6, 0],
         [0, 0, 1, 0, 5, 0, 9, 3, 0],
         [9, 0, 4, 0, 6, 0, 0, 0, 5],
         [0, 7, 0, 3, 0, 0, 0, 1, 2],
         [1, 2, 0, 0, 0, 7, 4, 0, 0],
         [0, 4, 9, 2, 0, 6, 0, 0, 7]]

text_blinking = False


def draw_board(window, squares):
    window.fill((255, 255, 255))
    tile_width = window.get_width() / 9
    tile_height = window.get_height() / 9
    gap = tile_height
    # draw vertical lines
    for i in range(9):
        if i % 3 == 0 and i != 0:
            thickness = 4
        else:
            thickness = 1
        pygame.draw.line(window, (0, 0, 0), (i * tile_width, 0), (i * tile_width, window.get_height()), thickness)
        pygame.draw.line(window, (0, 0, 0), (0, i * tile_height), (window.get_width(), i * tile_height), thickness)

    # font = pygame.font.SysFont('Arial', 40)
    # for i in range(9):
    #     for j in range(9):
    #         num = font.render(str(board[j][i]), True, (0, 0, 0))
    #         window.blit(num, (i * gap + 6, j * gap + 6))
    for i in range(9):
        for j in range(9):
            squares[i][j].draw(window)


class Square:
    def __init__(self, value, row, col, dimensions):
        self.value = value
        self.temp = 0
        self.row = row
        self.col = col
        self.width = dimensions[0] / 9
        self.height = dimensions[1] / 9
        self.selected = False

    def draw(self, window):
        font = pygame.font.SysFont('Arial', 40)
        number = font.render(str(self.value), True, (0, 0, 0))
        underscore = font.render('_', True, (0, 0, 0))
        if self.selected:
            pygame.draw.rect(window, (0, 255, 0),
                             (self.row * self.width, self.col * self.height, self.width, self.width))
            if self.value == 0:
                if text_blinking:
                    window.blit(underscore, (self.row * self.width, self.col * self.height))
        if self.value != 0:
            window.blit(number, (self.row * self.width, self.col * self.height))


def clicked_square(squares, x, y):
    row = x / (66.666)
    col = y / (66.666)
    print(str(row) + ' ' + str(col))
    print(squares[int(col)][int(row)].value)
    for i in range(9):
        for j in range(9):
            squares[i][j].selected = False
    squares[int(col)][int(row)].selected = True


def main():
    print('Just Testing')
    pygame.init()
    window = pygame.display.set_mode((600, 600))
    clock = pygame.time.Clock()
    blink_timer = 0

    running = True
    squares = [[Square(board[i][j], j, i, (window.get_width(), window.get_height())) for j in range(9)] for i in
               range(9)]
    mouse_x = None
    mouse_y = None
    global text_blinking

    while running:

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    print(str(mouse_x) + ' ' + str(mouse_y))
                    clicked_square(squares, mouse_x, mouse_y)

        draw_board(window, squares)
        pygame.display.update()
        clock.tick(30)

        blink_timer += 1
        if blink_timer == 15:
            blink_timer = 0
            if text_blinking:
                text_blinking = False
            else:
                text_blinking = True


main()
