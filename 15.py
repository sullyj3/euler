#https://projecteuler.net/problem=15
class grid_routes_solver(object):
    '''could be improved by dynamically altering grid size on an as needed 
    basis, rather than defining it at instantiation.'''

    def __init__(self, side_length):
        #creates a 2 dimensional square grid. purpose of the grid is for each coord to hold
        #a number representing the number of valid routes to get there
        #makes it a square with side length as the max dimension of the rectangle 

        #side_length specifies the maximum grid size that can be solved

        self.grid = [[None for y_pos in range(side_length+1)] for x_pos in range(side_length+1)]

    def grid_recurse(self, x, y):
        '''returns number of possible routes to a given integer coordinate, moving
        only right and down along integer spaced gridlines
        make sure x and y are within bounds specified by self.
        '''

        #read from existing grid to prevent unnecessary repetition
        preexisting = self.grid[x][y]
        if preexisting:
            return preexisting
            
        if 0 in (x,y):
            #any coord along y=0 or x=0 has only one valid route - a horizontal or
            #vertical line from the origin to that coord.

            self.grid[x][y] = 1
            return 1

        else:
            #number valid routes for given coordinates = sum of valid routes to its two preceding coordinates (above and to the left)

            num_routes = self.grid_recurse(x-1,y) + self.grid_recurse(x,y-1)
            self.grid[x][y] = num_routes

            #it'll be the same for the same rectangle on its side
            self.grid[y][x] = num_routes
            return num_routes
