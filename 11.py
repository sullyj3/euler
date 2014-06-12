def max_product(seq,length=4):
    prod_list = []
    for start_ind in range(len(seq)-length+1):
        prod = 1
        for i in seq[start_ind:start_ind+length]:
            prod *= i
        prod_list.append(prod)
    return max(prod_list)

grid = open("11_data")
lines = grid.readlines()

#convert each row to list of ints
lines = [[int(i) for i in line] for line in [line.rstrip('\n').split() for line in lines]]

def grid_h_max_product(grid):
    '''grid is a 2 dimensional list (list of rows)'''
    h_products = []
    for row in grid:
        h_products.append(max_product(row))
    return max(h_products)

def grid_v_max_product(grid):
    v_products = []
    grid_width = len(grid[0])
    for col_pos in range(grid_width):
        col = [row[col_pos] for row in grid]
        v_products.append(max_product(col))
    return max(v_products)

def grid_ddr_max_product(grid):
    #diagonal down right

    ddr_products = []

    grid_width = len(grid[0])

    #place starting position on left of grid, 4 above the bottom
    diag_sy = len(grid)-4

    #append max product of all diagonals of length 4 or greater which begin
    #on left hand side and move diagonally down right
    while diag_sy > 0:
        
        #define cursor variables
        diag_posy = diag_sy
        diag_posx = 0

        current_diag = []
        while diag_posy < len(grid):
            current_diag.append(grid[diag_posy][diag_posx])

            diag_posy += 1
            diag_posx += 1

        ddr_products.append(max_product(current_diag))
        diag_sy -= 1

    #append max product of all diagonals of length 4 or greater which begin
    #at top and move diagonally down right
    diag_sx = 0

    while diag_sx < grid_width-4:
        diag_posy = 0
        diag_posx = diag_sx
        current_diag = []
        while diag_posx < grid_width:
            current_diag.append(grid[diag_posy][diag_posx])

            diag_posy += 1
            diag_posx += 1

        ddr_products.append(max_product(current_diag))
        diag_sx += 1

    return max(ddr_products)

def grid_ddl_max_product(grid):
    #diagonal down left

    ddr_products = []

    grid_width = len(grid[0])

    #place starting position on right of grid, 4 above the bottom
    diag_sy = len(grid)-4

    #append max product of all diagonals of length 4 or greater which begin
    #on right hand side and move diagonally down left
    while diag_sy > 0:

        #define cursor variables
        diag_posy = diag_sy
        diag_posx = grid_width-1

        current_diag = []
        while diag_posy < len(grid):
            current_diag.append(grid[diag_posy][diag_posx])

            diag_posy += 1
            diag_posx -= 1

        ddr_products.append(max_product(current_diag))
        diag_sy -= 1

    #append max product of all diagonals of length 4 or greater which begin
    #at top and move diagonally down left
    diag_sx = grid_width - 1

    while diag_sx > 3:
        diag_posy = 0
        diag_posx = diag_sx
        current_diag = []
        while diag_posx >= 0:
            current_diag.append(grid[diag_posy][diag_posx])

            diag_posy += 1
            diag_posx -= 1

        ddr_products.append(max_product(current_diag))
        diag_sx -= 1

    return max(ddr_products)

print(
        max(grid_h_max_product(lines),
            grid_v_max_product(lines),
            grid_ddr_max_product(lines),
            grid_ddl_max_product(lines) 
            )
      )
