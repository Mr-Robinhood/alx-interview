def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid.

    :param grid: List of list of integers, where 0 represents water and 1 represents land.
    :return: The perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # Found land
                # Start with a cell perimeter of 4
                cell_perimeter = 4

                # Check the top cell
                if i > 0 and grid[i - 1][j] == 1:
                    cell_perimeter -= 1

                # Check the bottom cell
                if i < rows - 1 and grid[i + 1][j] == 1:
                    cell_perimeter -= 1

                # Check the left cell
                if j > 0 and grid[i][j - 1] == 1:
                    cell_perimeter -= 1

                # Check the right cell
                if j < cols - 1 and grid[i][j + 1] == 1:
                    cell_perimeter -= 1

                # Add the cell perimeter to the total
                perimeter += cell_perimeter

    return perimeter

