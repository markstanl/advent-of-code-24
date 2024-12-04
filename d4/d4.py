"""
--- Day 4: Ceres Search ---
My solution still seems quite brute force. I'm sure there is a more elegant way
to solve this problem. My solution is to check all possible directions for the
XMAS pattern. I then check all possible directions for the MAS pattern.
"""

def read_file(file_path):
    """
    Returns a 2d array of characters
    """
    with open(file_path, 'r') as f:
        file_lines = f.readlines()
    return [[char for char in l.strip()] for l in file_lines]


def check_up_left(board, i, j):
    """
    Returns True if there is a XMAS in the up left direction
    """
    if i < 3 or j < 3:
        return False
    if board[i - 1][j - 1] != 'M':
        return False
    if board[i - 2][j - 2] != 'A':
        return False
    if board[i - 3][j - 3] != 'S':
        return False
    return True


def check_up_right(board, i, j):
    """
    Returns True if there is a XMAS in the up right direction
    """
    if i < 3 or j > len(board[0]) - 4:
        return False
    if board[i - 1][j + 1] != 'M':
        return False
    if board[i - 2][j + 2] != 'A':
        return False
    if board[i - 3][j + 3] != 'S':
        return False
    return True


def check_down_left(board, i, j):
    """
    Returns True if there is a XMAS in the down left direction
    """
    if i > len(board) - 4 or j < 3:
        return False
    if board[i + 1][j - 1] != 'M':
        return False
    if board[i + 2][j - 2] != 'A':
        return False
    if board[i + 3][j - 3] != 'S':
        return False
    return True


def check_down_right(board, i, j):
    """
    Returns True if there is a XMAS in the down right direction
    """
    if i > len(board) - 4 or j > len(board[0]) - 4:
        return False
    if board[i + 1][j + 1] != 'M':
        return False
    if board[i + 2][j + 2] != 'A':
        return False
    if board[i + 3][j + 3] != 'S':
        return False
    return True


def check_left(board, i, j):
    """
    Returns True if there is a XMAS in the horizontal direction
    """
    if j < 3:
        return False
    if board[i][j - 1] != 'M':
        return False
    if board[i][j - 2] != 'A':
        return False
    if board[i][j - 3] != 'S':
        return False
    return True


def check_right(board, i, j):
    """
    Returns True if there is a XMAS in the horizontal direction
    """
    if j > len(board[0]) - 4:
        return False
    if board[i][j + 1] != 'M':
        return False
    if board[i][j + 2] != 'A':
        return False
    if board[i][j + 3] != 'S':
        return False
    return True


def check_up(board, i, j):
    """
    Returns True if there is a XMAS in the vertical direction
    """
    if i < 3:
        return False
    if board[i - 1][j] != 'M':
        return False
    if board[i - 2][j] != 'A':
        return False
    if board[i - 3][j] != 'S':
        return False
    return True


def check_down(board, i, j):
    """
    Returns True if there is a XMAS in the vertical direction
    """
    if i > len(board) - 4:
        return False
    if board[i + 1][j] != 'M':
        return False
    if board[i + 2][j] != 'A':
        return False
    if board[i + 3][j] != 'S':
        return False
    return True


def solve_part_one(board):
    """
    Returns the number of XMAS's on the board
    """
    xmas_count = 0
    for i, row in enumerate(board):
        for j, char in enumerate(row):
            if char == 'X':
                if check_up_left(board, i, j):
                    xmas_count += 1
                if check_up_right(board, i, j):
                    xmas_count += 1
                if check_down_left(board, i, j):
                    xmas_count += 1
                if check_down_right(board, i, j):
                    xmas_count += 1
                if check_left(board, i, j):
                    xmas_count += 1
                if check_right(board, i, j):
                    xmas_count += 1
                if check_up(board, i, j):
                    xmas_count += 1
                if check_down(board, i, j):
                    xmas_count += 1
    print(xmas_count)

def check_left_diagonal(board, i, j):
    """
    Returns True if there is a MAS in the left diagonal direction
    """
    if i < 1 or j < 1 or i > len(board) - 2 or j > len(board[0]) - 2:
        return False
    if board[i-1][j-1] == 'M' and board[i+1][j+1] == 'S':
        return True
    if board[i-1][j-1] == 'S' and board[i+1][j+1] == 'M':
        return True
    return False

def check_right_diagonal(board, i, j):
    """
    Returns True if there is a MAS in the right diagonal direction
    """
    if i < 1 or j < 1 or i > len(board) - 2 or j > len(board[0]) - 2:
        return False
    if board[i-1][j+1] == 'M' and board[i+1][j-1] == 'S':
        return True
    if board[i-1][j+1] == 'S' and board[i+1][j-1] == 'M':
        return True
    return False



def solve_part_two(board):
    """
    Finds for MAS in the shape of an X. Does so by looking for As, then
    checking their diagonals
    """
    x_mas_count = 0
    for i, row in enumerate(board):
        for j, char in enumerate(row):
            if char == 'A':
                if check_left_diagonal(board, i, j) and check_right_diagonal(board, i, j):
                    x_mas_count += 1
    print(x_mas_count)


if __name__ == '__main__':
    real = 'input.txt'
    example = 'example.txt'
    board = read_file(real)
    solve_part_two(board)
