#This function places the "Glider" pattern or any other known configuration from the Wikipedia page near the middle in the grid.
def center_grid(grid_size, configuration):
    x_start = (grid_size - configuration.shape[0]) // 2
    y_start = (grid_size - configuration.shape[1]) // 2
    grid[x_start:x_start + configuration.shape[0], y_start:y_start + configuration.shape[1]] = configuration
    return grid

def evolve(grid):  #The function updates the grid based on the rules of the game. 0 represents cells that are dead and 1 represents cells that are alive
    new_grid = np.zeros((grid_size, grid_size))
    for i in range(grid_size):
        for j in range(grid_size):
            #since the survival of the cells depends on their neigbors, lets define the neighbors
            left = grid[i, (j - 1) % grid_size]
            right = grid[i, (j + 1) % grid_size]
            top = grid[(i - 1) % grid_size, j]
            bottom = grid[(i + 1) % grid_size, j]
            top_left = grid[(i - 1) % grid_size, (j - 1) % grid_size]
            bottom_left = grid[(i + 1) % grid_size, (j - 1) % grid_size]
            top_right = grid[(i - 1) % grid_size, (j + 1) % grid_size]
            bottom_right = grid[(i + 1) % grid_size, (j + 1) % grid_size]
            neighbors = left + right + top + bottom + top_left + bottom_left + top_right + bottom_right

            if grid[i][j] == 0 and neighbors == 3: #Any dead cell with exactly three live neighbors becomes a live cell.
                new_grid[i][j] = 1
            elif grid[i][j] == 1 and neighbors < 2: #Any live cell with fewer than two live neighbors dies.
                new_grid[i][j] = 0
            elif grid[i][j] == 1 and neighbors > 3: #Any live cell with more than three live neighbors dies
                new_grid[i][j] = 0
            elif grid[i][j] == 1 and neighbors == 2 or neighbors == 3: #Any live cell with two or three live neighbors lives on to the next generation.
                new_grid[i][j] = 1
    grid[:] = new_grid #replace the grid with the evolved grid in order to be able to run the evolve function multiple times
