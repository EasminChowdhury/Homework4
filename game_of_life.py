import conway
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import copy
import sys

def game_of_life(k): 
    '''
    This script can be run by executing the command line python game_of_life.py 100 where k equals 100. 
    K is the number of times the code will generate a new image of the pattern based on the game rules. 
    Read the README file for more details
    Input: game_of_life 100
    Output: an animation where the glider pattern is run 100 times through the evolve function. 
    The animation shows every tenth step of every tenth run of the evolve function.
    '''
    #If the k passed from the command line is not a positive integer, it will display the below message and exit the program.
    if not isinstance(k, int) or k <= 0:
        print("Error: k must be a positive integer.")
        sys.exit(1)
        
    # create a figure and axis
    fig, ax = plt.subplots()

    #(grid_size can be adjusted):
    grid_size=20

    # Create a configuration that the game of life will run. Here the configuration being used is the glider pattern but that can be adjusted
    glider = np.array([[0, 1, 0], [0, 0, 1], [1, 1, 1]])
    configuration = glider

    #Create an empty grid of 20*20 or gridsize and place the "Glider" pattern or any other known configuration near the middle of the grid.
    grid = center_grid(grid_size, configuration)

    # create an image plot with a black and white colormap. Alive cells are colored black, and dead cells are white
    im = ax.imshow(grid, cmap='gray', vmin=0, vmax=1)

    def update(frame): #This function updates the frames. Each frame reflects the image after every 10th step of the evolve function.
        for i in range(10):
            evolve(grid) #The evolve function follows the game rules to determine which cells are alive or dead. 
        im.set_data(grid) #This creates an image after the evolve function has been iterated 10 times.
        return im, #returns the image to use in the animation 

    final_frame = grid.copy() # Create a snapshot of the last frame
    
    # Create a gif of the evolution from the initial state to the final state at a frame rate of 10 frames per second. There are k/10 frames since the image above shows every tenth step
    ani = animation.FuncAnimation(fig, update, frames=int(k/10), interval=10, blit=True, repeat=False)

    # create the writer. 10 frames per second
    writer = animation.PillowWriter(fps=10)

    # save the animation as a GIF
    ani.save('game_of_life.gif', writer=writer)

    # Save the final frame as an image (game_of_life.png)
    fig.set_size_inches(10,10)
    plt.imsave("game_of_life.png", final_frame, cmap='gray', vmin=0, vmax=1)

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
