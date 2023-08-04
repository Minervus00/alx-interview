#!/usr/bin/python3
"""Module for the Queen"""
from sys import exit, argv, setrecursionlimit
setrecursionlimit(5000)
# ================ Handle errors ========


def print_error(msg):
    """Prints an error message"""
    print(msg)
    exit(1)


if len(argv) != 2:
    print_error("Usage: nqueens N")
try:
    N = int(argv[1])
except Exception:
    print_error("N must be a number")

N = int(N)
if N < 4:
    print_error("N must be at least 4")

# ============ Solving the problem ===========
frontier = []
solution = []
placed = []
EMPTY = 0
dic = {'queens': 0}

board = []
for i in range(N):
    tmp = []
    for j in range(N):
        tmp.append(EMPTY)
    board.append(tmp[:])


# def print_board():
#     import numpy as np
#     print(np.array(board[::-1]))
#     print()


def is_valid(col, row):
    """Checks if the action is valid i.e if placing the queen
    at position = (col, row) doesn't threat already placed queens"""

    # Checking row
    if any(itm != EMPTY for itm in board[row]):
        return False

    # Check column
    for line in board:
        if line[col] != EMPTY:
            return False

    # Check diagonals
    for h in range(1, N):
        y = col + h
        if y < N:
            x = row + h
            if x < N and board[x][y] != EMPTY:
                return False
            x = row - h
            if y >= 0 and board[x][y] != EMPTY:
                return False
        y = col - h
        if y >= 0:
            x = row + h
            if x < N and board[x][y] != EMPTY:
                return False
            x = row - h
            if x >= 0 and board[x][y] != EMPTY:
                return False

    return True


def place_queen(c, r):
    if is_valid(c, r):
        dic["queens"] += 1
        solution.append([c, r])
        board[r][c] = 1

        if dic["queens"] == N:
            print(solution)
            # print_board()
            dic["queens"] -= 1
            solution.pop()
            board[r][c] = EMPTY
        else:
            # Move to next column
            explore_col(c + 1)


def explore_col(c):
    """Continue exploration by the beginning of the column c"""
    for r in range(N - 1, -1, -1):
        frontier.append((c, r))
    while frontier:
        col, row = frontier.pop()
        dic["cur_col"] = col
        # If the algorithm go back clean the board by removing useless
        # marked states
        while dic["prev_col"] > dic["cur_col"]:
            # print("colomn back")
            dic["queens"] -= 1
            c, r = solution.pop()
            board[r][c] = EMPTY
            dic["prev_col"] -= 1
        place_queen(col, row)
        dic["prev_col"] = col


def resolve():
    col = 0
    dic["cur_col"] = col
    dic["prev_col"] = col
    explore_col(col)


resolve()
