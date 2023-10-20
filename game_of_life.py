import conway
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import copy
import sys

def game_of_life(k): #This script can be run throgh executing the command line python game_of_life.py 100 where k equals 100
    
    #If the k passed from the command line is not positive integer, it will display an the below message and exit the program.
    if not isinstance(k, int) or k <= 0:
        print("Error: k must be a positive integer.")
        sys.exit(1)
        
    # create a figure and axis
    fig, ax = plt.subplots()

    # create a empty grid of 20*20 (grid_size can be adjusted):
    grid_size=20
    grid = np.zeros((grid_size, grid_size)) 

    # Create a configuration that the game of life will run. In here the configuration being used is glider but that can be adjusted
    glider = np.array([[0, 1, 0], [0, 0, 1], [1, 1, 1]])
    configuration = glider

    #Place the "Glider" pattern or any other known configuration near the middle in the grid.
    grid = center_grid(grid_size, configuration)

    # create an image plot with a black and white colormap. Alive cells are colored black, and dead cells white
    im = ax.imshow(grid, cmap='gray', vmin=0, vmax=1)

    def update(frame): #This function updates the frames. Each frame reflects the image after every 10th step of using the evolve function.
        for i in range(10):
            evolve(grid) #The evolve function follows the games rules to determine which cells are alive or dead. 
        im.set_data(grid) #This creates an image after evolve function has been iterated 10 times.
        return im, #returns the image to use in the animation 

    # Create a gif of the evolution from the initial state to the final state at a frame rate of 10 frames per second. There are k/10 frames since the image above shows every tenth step
    ani = animation.FuncAnimation(fig, update, frames=int(k/10), interval=10, blit=True, repeat=False)

    # create the writer. 10 frames per second
    writer = animation.PillowWriter(fps=10)

    # save the animation as a GIF
    ani.save('game_of_life.gif', writer=writer)

    # close the plot window
    plt.close()
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python game_of_life.py <k>")
        sys.exit(1)

    try:
        k = int(sys.argv[1])
        game_of_life(k)
    except ValueError:
        print("Error: k must be a positive integer.")
        sys.exit(1)