#!/usr/bin/python3
"""Define a nqueens N"""


import sys


def board_deepcopy(board)
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return board


def init_board(n):
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return (board)


def solve(queens, available_rows):
    if not available_rows:
        return [queens]
    else:
        n = available_rows[0]
        solutions = []
        for i in range(N):
            if can_place(queens, n, i):
                solutions.extend(solve(queens + [(n, i)], available_rows[1:]))
        return solutions


def print_solutions(solutions):
    for i, solution in enumerate(solutions):
        print(f"Solution {i + 1}:")
        for n, col in solution:
            print(f"[ {n}, {col} ]", end='')
        print()
