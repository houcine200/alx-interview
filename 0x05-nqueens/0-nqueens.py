#!/usr/bin/python3
from sys import argv, exit


def solveNQueens(n):
    def could_place(row, col):
        for i in range(row):
            if (board[i] == col or
                board[i] - i == col - row or
                    board[i] + i == col + row):
                return False
        return True

    def place_queens(n, row):
        if row == n:
            result.append(board[:])
            return
        for col in range(n):
            if could_place(row, col):
                board[row] = col
                place_queens(n, row + 1)
                board[row] = 0

    result = []
    board = [0] * n
    place_queens(n, 0)
    return result


if __name__ == '__main__':
    if len(argv) != 2:
        print('Usage: nqueens N')
        exit(1)

    try:
        n = int(argv[1])

        if n < 4:
            print('N must be at least 4')
            exit(1)

    except ValueError:
        print('N must be a number')
        exit(1)

solutions = solveNQueens(n)
for sol in solutions:
    print([[row, col] for row, col in enumerate(sol)])
