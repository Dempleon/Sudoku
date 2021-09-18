import random

import pygame
from pygame.locals import *
import copy

board = [[7, 8, 0, 4, 0, 0, 1, 2, 0],
         [6, 0, 0, 0, 7, 5, 0, 0, 9],
         [0, 0, 0, 6, 0, 1, 0, 7, 8],
         [0, 0, 7, 0, 4, 0, 2, 6, 0],
         [0, 0, 1, 0, 5, 0, 9, 3, 0],
         [9, 0, 4, 0, 6, 0, 0, 0, 5],
         [0, 7, 0, 3, 0, 0, 0, 1, 2],
         [1, 2, 0, 0, 0, 7, 4, 0, 0],
         [0, 4, 9, 2, 0, 6, 0, 0, 7]]

blank_board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0]]

rand_board = [[4, 3, 5, 2, 6, 9, 7, 8, 1],
              [6, 8, 2, 5, 7, 1, 4, 9, 3],
              [1, 9, 7, 8, 3, 4, 5, 6, 2],
              [8, 2, 6, 1, 9, 5, 3, 4, 7],
              [3, 7, 4, 6, 8, 2, 9, 1, 5],
              [9, 5, 1, 7, 4, 3, 6, 2, 8],
              [5, 1, 9, 3, 2, 6, 8, 7, 4],
              [2, 4, 8, 9, 5, 7, 1, 3, 6],
              [7, 6, 3, 4, 1, 8, 2, 5, 9]]

test_board = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
              [5, 2, 0, 0, 0, 0, 0, 0, 0],
              [0, 8, 7, 0, 0, 0, 0, 3, 1],
              [0, 0, 3, 0, 1, 0, 0, 8, 0],
              [9, 0, 0, 8, 6, 3, 0, 0, 5],
              [0, 5, 0, 0, 9, 0, 6, 0, 0],
              [1, 3, 0, 0, 0, 0, 2, 5, 0],
              [0, 0, 0, 0, 0, 0, 0, 7, 4],
              [0, 0, 5, 2, 0, 6, 3, 0, 0]]

text_blinking = False


def draw_board(window, squares):
    window.fill((255, 255, 255))
    tile_width = window.get_width() / 9
    tile_height = (window.get_height() - 100) / 9
    gap = tile_height
    # draw vertical lines
    for i in range(9):
        if i % 3 == 0 and i != 0:
            thickness = 4
        else:
            thickness = 1
        pygame.draw.line(window, (0, 0, 0), (i * tile_width, 0), (i * tile_width, window.get_height() - 100), thickness)

    for i in range(10):
        if i % 3 == 0 and i != 0:
            thickness = 4
        else:
            thickness = 1

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
    def __init__(self, value, row, col, side):
        self.value = value
        self.temp = 0
        self.row = row
        self.col = col
        self.side_length = side / 9
        self.selected = False

    def draw(self, window):
        font = pygame.font.SysFont('Arial', 40)
        number = font.render(str(self.value), True, (0, 0, 0))
        underscore = font.render('_', True, (0, 0, 0))
        if self.selected:
            pygame.draw.rect(window, (0, 255, 0),
                             (self.row * self.side_length, self.col * self.side_length, self.side_length,
                              self.side_length))
            # if self.value == 0:
            #     if text_blinking:
            #         window.blit(underscore, (self.row * self.side_length, self.col * self.side_length))
            # elif text_blinking:
            #     window.blit(number, (self.row * self.side_length, self.col * self.side_length))
            if text_blinking:
                if self.value == 0:
                    window.blit(underscore, (self.row * self.side_length, self.col * self.side_length))
                else:
                    window.blit(number, (self.row * self.side_length, self.col * self.side_length))
        else:
            if self.value != 0:
                window.blit(number, (self.row * self.side_length, self.col * self.side_length))


def blank_board(squares):
    for i in range(9):
        for j in range(9):
            squares[i][j].value = 0


def shuffle_rows(squares):
    rand_group = random.randint(0, 2)
    row1 = 3 * rand_group + random.randint(0, 2)
    row2 = 3 * rand_group + random.randint(0, 2)
    while row1 == row2:
        row1 = 3 * rand_group + random.randint(0, 2)

    for i in range(9):
        temp = squares[row1][i].value
        squares[row1][i].value = squares[row2][i].value
        squares[row2][i].value = temp


def shuffle_cols(squares):
    rand_group = random.randint(0, 2)
    col1 = 3 * rand_group + random.randint(0, 2)
    col2 = 3 * rand_group + random.randint(0, 2)

    while col1 == col2:
        col1 = 3 * rand_group + random.randint(0, 2)

    for i in range(9):
        temp = squares[i][col1].value
        squares[i][col1].value = squares[i][col2].value
        squares[i][col2].value = temp


# easy board 25 filled in squares
def new_board(squares, difficulty):
    num_known = difficulty * 10

    for i in range(9):
        for j in range(9):
            squares[i][j].value = rand_board[i][j]

    for i in range(100):
        shuffle_rows(squares)
        shuffle_cols(squares)

    for i in range(81 - num_known):
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        while squares[row][col].value == 0:
            row = random.randint(0, 8)
            col = random.randint(0, 8)

        squares[row][col].value = 0


def clicked_square(squares, x, y):
    row = x / 66.666
    col = y / 66.666
    print(str(row) + ' ' + str(col))
    print(squares[int(col)][int(row)].value)
    for i in range(9):
        for j in range(9):
            squares[i][j].selected = False
    squares[int(col)][int(row)].selected = True
    # for event in pygame.event.get():
    #     if event.type == KEYDOWN:
    #         if event.key == K_1:
    #             squares[row][col].value = 1


def print_board(squares):
    for i in range(9):
        for j in range(9):
            print(squares[i][j].value, end='')
        print('')


def solve(squares):
    print('Solving the squares')
    if is_done(squares):
        return True

    is_empty = find_empty(squares)
    if is_empty:
        print_board(squares)
        for i in range(1, 10):
            print(i)
            if valid(i, squares, is_empty[0], is_empty[1]):
                squares[is_empty[0]][is_empty[1]].value = i

                if is_done(squares):
                    return True
                if solve(squares):
                    return True
        squares[is_empty[0]][is_empty[1]].value = 0
        return False


def find_empty(squares):
    for i in range(9):
        for j in range(9):
            if squares[i][j].value == 0:
                print('empty ' + str(i) + ' ' + str(j))
                return [i, j]

    return False


def is_done(squares):
    for i in range(9):
        for j in range(9):
            # print(squares[i][j].value)
            if squares[i][j].value == 0:
                print('not done')
                return False

    print('done')
    return True


def valid(value, squares, row, col):
    for i in range(9):
        if squares[row][i].value == value:
            return False
        if squares[i][col].value == value:
            return False

    box_x = row // 3
    box_y = col // 3

    for i in range(box_x * 3, box_x * 3 + 3):
        for j in range(box_y * 3, box_y * 3 + 3):
            if squares[i][j].value == value and (i != row and j != col):
                return False
            # if squares[i][j].value == value:
            #     return False

    return True


def main():
    print('Just Testing')
    pygame.init()
    window = pygame.display.set_mode((600, 700))
    clock = pygame.time.Clock()
    blink_timer = 0

    running = True
    squares = [[Square(rand_board[i][j], j, i, window.get_width()) for j in range(9)] for i in
               range(9)]
    new_board(squares, 4)
    # mouse_x = None
    # mouse_y = None
    selected_something = False
    selected = [-1, -1]
    global text_blinking

    # solve(squares)

    while running:

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if selected_something:
                    if event.key == K_0:
                        squares[int(selected[0])][int(selected[1])].value = 0
                    if event.key == K_1:
                        squares[int(selected[0])][int(selected[1])].value = 1
                    if event.key == K_2:
                        squares[int(selected[0])][int(selected[1])].value = 2
                    if event.key == K_3:
                        squares[int(selected[0])][int(selected[1])].value = 3
                    if event.key == K_4:
                        squares[int(selected[0])][int(selected[1])].value = 4
                    if event.key == K_5:
                        squares[int(selected[0])][int(selected[1])].value = 5
                    if event.key == K_6:
                        squares[int(selected[0])][int(selected[1])].value = 6
                    if event.key == K_7:
                        squares[int(selected[0])][int(selected[1])].value = 7
                    if event.key == K_8:
                        squares[int(selected[0])][int(selected[1])].value = 8
                    if event.key == K_9:
                        squares[int(selected[0])][int(selected[1])].value = 9
                    if event.key == K_e:
                        print('new easy')
                        new_board(squares, 4)
                    if event.key == K_c:
                        print('shuffle columns')
                        shuffle_cols(squares)
                    if event.key == K_n:
                        print('new board')
                        blank_board(squares)
                    if event.key == K_r:
                        print('shuffle rows')
                        shuffle_rows(squares)
                    if event.key == K_s:
                        print('solving')
                        if solve(squares):
                            print_board(squares)
                        else:
                            print('no solution')

                    draw_board(window, squares)
                    blink_timer = 0
                    text_blinking = True
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if mouse_y and mouse_y <= window.get_width():
                        selected_something = True
                    else:
                        selected_something = False
                    selected[1] = mouse_x / 66.666
                    selected[0] = mouse_y / 66.666
                    # print(str(mouse_x) + ' ' + str(mouse_y))
                    if mouse_y <= 600:
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
