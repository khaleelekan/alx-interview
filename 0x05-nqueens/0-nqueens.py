#!/usr/bin/python3
"""N queens solution finder module.
"""
import sys

solutions = []
n = 0
pos = []

def get_input():
    """Retrieves and validates this program's argument."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n

def is_attacking(pos0, pos1):
    """Checks if the positions of two queens are in an attacking mode."""
    return (pos0[0] == pos1[0] or pos0[1] == pos1[1] or
            abs(pos0[0] - pos1[0]) == abs(pos0[1] - pos1[1]))

def build_solution(row, group):
    """Builds a solution for the n queens problem."""
    if row == n:
        solutions.append(group.copy())
        return
    for col in range(n):
        pos = (row, col)
        if all(not is_attacking(pos, q) for q in group):
            group.append(pos)
            build_solution(row + 1, group)
            group.pop()

def get_solutions():
    """Gets the solutions for the given chessboard size."""
    build_solution(0, [])

n = get_input()
get_solutions()
for solution in solutions:
    print(solution)

