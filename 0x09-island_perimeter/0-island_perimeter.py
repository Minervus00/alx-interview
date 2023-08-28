#!/usr/bin/python3
"""Module containing the island_perimeter function"""


def island_perimeter(grid):
    """Computes and Returns the perimeter of an island made with horizontally
    or vertically conneted cells"""
    perim = neighbs = 0
    cells = []
    tested_cells = []
    nrows, ncols = len(grid), len(grid[0])

    # Search the first cell of the island
    for j in range(nrows):
        for i in range(ncols):
            if grid[j][i] == 1:
                cells.append((j, i))
                break
        else:  # Executed if no break reached in for loop same indented above
            continue
        break

    # Use Breadth First Search starting to the 1st cell of island
    # to reach all connected cells;
    # For each cell in cells, count its' neighbors and this cell implication
    # in the total perimeter is about 4 - number_of_neighbors.
    while(cells):
        j, i = cells.pop(0)
        tested_cells.append((j, i))
        for y, x in [(j, i-1), (j, i+1), (j-1, i), (j+1, i)]:
            if 0 <= y < nrows and 0 <= x < ncols and grid[y][x] == 1:
                # add the current neighbor in cells if it is
                # not in cells (waiting to be processed) and
                # not in tested_cells (already processed)
                if (y, x) not in tested_cells and (y, x) not in cells:
                    cells.append((y, x))
                neighbs += 1
        perim += 4 - neighbs
        neighbs = 0

    return perim
