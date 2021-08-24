test_board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

example_board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def solve(board):
    empty = find_empty(board)
    if not empty:
        return True
    else:
        row, col = empty

    for i in range(1, 10):
        if valid(board, i, row, col):
            board[row][col] = i

            # recursive
            if solve(board):
                return True
            else:
                board[row][col] = 0

    return False


def valid(board, value, row, col):
    # for i in range(9):
    #     # check row
    #     if board[row][i] == value:
    #         return False
    #     # check column
    #     if board[i][col] == value:
    #         return False
    #     # check box
    for i in range(9):
        if board[row][i] == value and row != i:
            return False
        if board[i][col] == value and col != i:
            return False

    for i in range(col // 3 * 3, col // 3 * 3 + 3):
        for j in range(row // 3 * 3, row // 3 * 3 + 3):
            if board[i][j] == value:
                return False

    box_x = row // 3
    box_y = col // 3

    for i in range(box_x * 3, box_x * 3 + 3):
        for j in range(box_y * 3, box_y * 3 + 3):
            if board[i][j] == value and (i != row and j != col):
                return False

    return True


def print_board(board):
    # print('_________________')
    # for row in board:
    #     for num in row:
    #         print(num, end=' ')
    #     print('')
    # print('_________________')
    # print('-----------------')
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print('---------------------')
        for j in range(len(board)):
            if j % 3 == 0 and j != 0:
                print('|', end=' ')
            print(board[i][j], end=' ')
        print('')

    pass


def find_empty(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col

    return None

# print_board(example_board)
# print(valid(example_board, 7, 2, 2))
# print(valid(example_board, 1, 1, 1))
# print(valid(example_board, 2, 4, 4))
