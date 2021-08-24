import pygame
from Board import *
import Tile
import Sudoku_solver
import time

def draw_win(window, board, time):
    window.fill((255, 255, 255))

    # draw time
    seconds = time % 60
    minutes = time // 60
    clock = ' ' + str(minutes) + ':' + str(seconds)
    time_text = pygame.font.SysFont('comicsans', 40)
    text = time_text.render('Time: ' + clock, True, (0, 0, 0))
    window.blit(text, (540 - 160, 560))

    board.draw(window)

def main():
    pygame.init()
    window = pygame.display.set_mode((540, 600))
    pygame.display.set_caption('Sudoku')
    board = Board(9, 9, 540, 540)
    key = None
    run = True
    start = time.time()

    while run:
        play_time = round(time.time() - start)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_DELETE:
                    board.clear()
                    key = None
                if event.key == pygame.K_RETURN:
                    i, j = board.highlighted
                    if board.tiles[i][j].temp != 0:
                        if board.place(board.tiles[i][j].temp):
                            print("Success")
                        else:
                            print("Wrong")
                        key = None

                        if board.is_finished():
                            print("Game over")
                            run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked = board.click(pos[0], pos[1])
                if clicked:
                    board.select(clicked[0], clicked[1])
                    key = None

        if board.highlighted and key is not None:
            board.sketch(key)

        draw_win(window, board, play_time)
        pygame.display.update()

main()
pygame.quit()

