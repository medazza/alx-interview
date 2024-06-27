def island_perimeter(grid):
    """
    Computes the perimeter of an island with no lakes.

    Args:
        grid (list): A 2D list representing the island, where 0 represents water and 1 represents land.

    Returns:
        int: The total perimeter of the island.
    """
    if not isinstance(grid, list) or not all(isinstance(row, list) for row in grid):
        return 0

    perimeter = 0
    num_rows, num_cols = len(grid), len(grid[0])

    for i in range(num_rows):
        for j in range(num_cols):
            if grid[i][j] == 1:
                # Check the four adjacent cells
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                if j == num_cols - 1 or grid[i][j+1] == 0:
                    perimeter += 1
                if i == num_rows - 1 or grid[i+1][j] == 0:
                    perimeter += 1
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1

    return perimeter
