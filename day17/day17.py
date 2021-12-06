# --- Advent of Code 2020 --- 
# --- Day 17: Conway Cubes ---
#       ____
#     _|____|_
#     ( '<' )
#  >-(   o   )-<
#   (    o    )
#  (     o     )

import copy

def read_input(
    filename: str,
    inf_grid: int,
    sup_grid: int,
) -> dict:
    """This function reads the input file and returns the data in
    the appropriate format.

    Args:
        filename (str): The name of the file to read.
        inf_grid (int): The inferior limit of the grid to read.
        sup_grid (int): The superior limit of the grid to read.

    Returns:
        dict: The input data for the puzzle
    """
    input_file = open(filename, 'r')

    grid_dict = {}

    z = 0

    grid_dict[z] = {}

    for y in range(-inf_grid, sup_grid+1):
        grid_dict[z][y] = {}
        for x in range(-inf_grid, sup_grid+1):
            grid_dict[z][y][x] = 0

    x = -inf_grid
    y = -inf_grid
    z = 0

    for line in input_file:
        temp = line.split()[0]
        temp_grid = []
        for elem in temp:
            grid_dict[z][y][x] = elem
            x = x + 1
        y = y + 1
        x = -inf_grid

    return grid_dict

def plot_grid(
    grid_dict: dict, 
    z: int,
) -> None:
    """This function plots the grid.

    Args:
        grid_dict (dict): The Conway Cubes grid.
        z (int): the layer of z to plot.
    """
    min_y = min(grid_dict[z].keys())
    max_y = max(grid_dict[z].keys())
    for y in range(min_y, max_y + 1):
        temp_list = []
        min_x = min(grid_dict[z][y].keys())
        max_x = max(grid_dict[z][y].keys())
        for x in range(min_x, max_x + 1):
            temp_list.append(grid_dict[z][y][x])
        print(temp_list)


def create_next_layer(
    grid_dict: dict
) -> dict:
    """This function creates the grid for the new iteration.

    Args:
        grid_dict (dict): The Conway Cubes grid.

    Returns:
        dict: The updated Conway Cubes grid.
    """
    min_z = min(grid_dict.keys()) - 1
    max_z = max(grid_dict.keys()) + 1
    min_y = min(grid_dict[0].keys()) - 1
    max_y = max(grid_dict[0].keys()) + 1
    min_x = min(grid_dict[0][0].keys()) - 1
    max_x = max(grid_dict[0][0].keys()) + 1
    new_grid_dict = copy.deepcopy(grid_dict)
    for z in range(min_z, max_z + 1):
        if z not in new_grid_dict:
            new_grid_dict[z] = {}
        for y in range(min_y, max_y + 1):
            if y not in new_grid_dict[z]:
                new_grid_dict[z][y] = {}
            for x in range(min_x, max_x + 1):
                if x not in new_grid_dict[z][y]:
                    new_grid_dict[z][y][x] = '.'

    return(new_grid_dict)

def update_grid(
    grid_dict: dict,
) -> dict:
    """This function updates the grid for the new iteration
    following a set of rules.

    Args:
        grid_dict (dict): The Conway Cubes grid.

    Returns:
        dict: The updated Conway Cubes grid.
    """
    min_z = min(grid_dict.keys())
    max_z = max(grid_dict.keys())
    min_y = min(grid_dict[0].keys())
    max_y = max(grid_dict[0].keys())
    min_x = min(grid_dict[0][0].keys())
    max_x = max(grid_dict[0][0].keys())
    new_grid_dict = copy.deepcopy(grid_dict)

    for z in range(min_z, max_z + 1):
        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                current_status = str(grid_dict[z][y][x])
                count_activated  = 0
                for i in range(-1,1+1):
                    for j in range(-1,1+1):
                        for k in range(-1,1+1):
                            if [i,j,k] != [0,0,0]:
                                try:
                                    neighbor_status = str(grid_dict[z+k][y+j][x+i])
                                    if neighbor_status == '#':
                                        count_activated = count_activated + 1
                                except KeyError:
                                    pass

                if current_status == '#' and count_activated != 2 and count_activated !=3:
                    new_grid_dict[z][y][x] = '.'
                elif current_status == '.' and count_activated ==3:
                    new_grid_dict[z][y][x] = '#'
    
    return(new_grid_dict)


def part1(
    input_dict: dict,
) -> int:
    """This function maps the number of active cubes of the Conway Cubes
    after a sequence of iterations.

    Args:
        input_dict (dict): The puzzle input data.

    Returns:
        int: The number of active cubes.
    """

    current_grid = copy.deepcopy(input_dict)

    plot_grid(input_dict, 0)

    for iteration in range(1,6+1):
        new_grid_dict = create_next_layer(current_grid)
        # plot_grid(new_grid_dict, 0)
        updated_grid = update_grid(new_grid_dict)
        # plot_grid(updated_grid, 0)
        current_grid = copy.deepcopy(updated_grid)

    count_activated = 0

    for z in current_grid.keys():
        for y in current_grid[z].keys():
            for x in current_grid[z][y].keys():
                if current_grid[z][y][x] == '#':
                    count_activated = count_activated + 1
    return(count_activated)
        
# puzzle_input = read_input('example17.txt', 1, 1)
puzzle_input = read_input('input17.txt', 4, 3)

#Part 1 Solution
part1_solution = part1(puzzle_input)
print("Part 1 Solution: %s"%part1_solution)