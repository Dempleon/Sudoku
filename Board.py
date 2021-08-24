import pygame
from Sudoku_solver import valid, solve
from Tile import *


class Board:
    # board = [
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0]
    # ]

    board = [[7, 8, 0, 4, 0, 0, 1, 2, 0],
             [6, 0, 0, 0, 7, 5, 0, 0, 9],
             [0, 0, 0, 6, 0, 1, 0, 7, 8],
             [0, 0, 7, 0, 4, 0, 2, 6, 0],
             [0, 0, 1, 0, 5, 0, 9, 3, 0],
             [9, 0, 4, 0, 6, 0, 0, 0, 5],
             [0, 7, 0, 3, 0, 0, 0, 1, 2],
             [1, 2, 0, 0, 0, 7, 4, 0, 0],
             [0, 4, 9, 2, 0, 6, 0, 0, 7]]

    def __init__(self, rows, cols, width, height):
        self.rows = rows
        self.columns = cols
        self.width = width
        self.height = height
        self.model = None
        self.highlighted = None
        self.tiles = [[Tile(self.board[i][j], i, j, width, height) for j in range(cols)] for i in range(rows)]

    def update_model(self):
        self.model = [[self.tiles[i][j].value for j in range(self.columns)] for i in range(self.rows)]

    def place(self, val):
        row, col = self.highlighted
        if self.tiles[row][col].value == 0:
            self.tiles[row][col].set(val)
            self.update_model()

            if valid(self.model, val, row, col) and solve(self.model):
                return True
            else:
                self.tiles[row][col].set(0)
                self.tiles[row][col].set_temp(0)
                self.update_model()
                return False

    def sketch(self, value):
        row, col = self.highlighted
        self.tiles[row][col].set_temp(value)

    def draw(self, window):

        gap = self.width / 9
        # Draw tiles
        for i in range(9):
            for j in range(9):
                self.tiles[i][j].draw(window)

        for i in range(10):
            if i % 3 == 0 and i != 0:
                line_thickness = 4
            else:
                line_thickness = 1

            pygame.draw.line(window, (0, 0, 0), (0, i * gap), (self.width, i * gap), line_thickness)
            pygame.draw.line(window, (0, 0, 0), (i * gap, 0), (i * gap, self.height), line_thickness)

    def select(self, row, column):
        for i in range(9):
            for j in range(9):
                self.tiles[i][j].highlighted = False
        self.tiles[row][column].highlighted = True
        self.highlighted = (row, column)

    def clear(self):
        row, col = self.highlighted
        if self.tiles[row][col].value == 0:
            self.tiles[row][col].set_temp(0)

    def click(self, x, y):
        if x < self.width and y < self.height:
            gap = self.width / 9
            x_pos = x // gap
            y_pos = y // gap
            return int(y_pos), int(x_pos)
        else:
            return None

    def is_finished(self):
        for i in range(9):
            for j in range(9):
                if self.tiles[i][j].value == 0:
                    return False
        return True
