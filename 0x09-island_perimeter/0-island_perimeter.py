#!/usr/bin/python3
"""
Perimeter of the island
"""


def island_perimeter(grid):
    """Returns the perimeter of the island"""
    if not grid:
        return 0

    perimeter = 0
    rows, colum = len(grid), len(grid[0])

    for r in range(rows):
        for c in range(colum):
            if grid[r][c] == 1:
                perimeter += 4

                # Check adjacent cells (up, down, left, and right)
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2

    return perimeter
