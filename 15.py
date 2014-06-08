#https://projecteuler.net/problem=15
#using globals isn't very elegant. maybe ask about a nicer way of doing it

def gen_grid(width, height):
    #creates a 2 dimensional grid. purpose of the grid is for each coord to hold
    #a number representing the number of valid routes to get there
    #makes it a square with side length as the max dimension of the rectangle 

    side_length = max((width,height))

    grid = [[None for y_pos in range(side_length+1)] for x_pos in range(side_length+1)]
    return grid


def grid_routes(width, height):
    global grid
    grid = gen_grid(width,height)

    return grid_recurse(width,height)

def grid_recurse(width, height):
    '''returns number of possible routes to a given integer coordinate, moving
    only right and down along integer spaced gridlines'''

    #read from existing grid to prevent unnecessary repetition
    global grid
    preexisting = grid[width][height]
    if preexisting:
        return preexisting
        
    if 0 in (width,height):
        #any coord along y=0 or x=0 has only one valid route - a horizontal or
        #vertical line from the origin to that coord.

        grid[width][height] = 1
        return 1

    else:
        #number valid routes for given coordinates = sum of valid routes to its two preceding coordinates (above and to the left)

        val = grid_recurse(width-1,height) + grid_recurse(width,height-1)
        grid[width][height] = val
        #it'll be the same for the same rectangle on its side
        grid[height][width] = val
        return val
