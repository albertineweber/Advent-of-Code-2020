import numpy as np

arq = open('input17.txt', 'r')

def check_adjacents(grid):
    global x0, y0, z0

    new_grid = np.zeros((z0, x0, y0))
    new_grid = np.where(new_grid==0, ".", new_grid) 

    count_ocup = 0
    
    if coordinate in coordinates:
        new_state = states[coordinates.index(coordinate)]
    else:
        new_state = 0

    for i in range(-1,1+1):
        for j in range(-1,1+1):
            for k in range(-1,1+1):
              if i != 0 or j != 0 or k != 0:
                neighbor = [x+i, y+j, z+k]

                if neighbor in coordinates:
                    if states[coordinates.index(neighbor)] == 1:
                        #print(states[coordinates.index(neighbor)])
                        count_ocup = count_ocup + 1
    
    #print(coordinate, new_state, count_ocup)

    if new_state == 1 and count_ocup != 2 and count_ocup != 3:
        new_state = 0
    
    if new_state == 0 and count_ocup == 3:
        new_state = 1

    return(new_state)

x = -1
y = 1 
z = 0

coordinates = []
states = []
grid = []
temp_grid = []

for line in arq:
    temp = line.split()[0]
    temp_grid = []
    for elem in temp:
        temp_grid.append(elem)
        x = x + 1
    grid.append(temp_grid)
    y = y - 1
    x = -1


x0 = len(grid[0]) + 2*7
y0 = len(grid) + 2*7
z0 = 1 + 2*7

zeros_array = np.zeros((z0, x0, y0))
zeros_array = np.where(zeros_array==0, ".", zeros_array) 


for x in range(0, len(grid)):
    for y in range(0, len(grid[0])):
        zeros_array[7, 7+x, 7+y] = grid[x][y]

grid = zeros_array

print(zeros_array[7])

#for i in range(0, len(states)):
    #print(coordinates[i], states[i])

#temp_grid = ["." for i in range(0, len(grid)*7)]
#gridxy = [temp_grid for i in range(0, len(grid)*7)]
#grids = [gridxy for i in range(0, len(grid)*7)]

#print(temp_grid)
#print(gridxy)
#print(grids)


#dict_grid = {0: temp_grid}
#print(dict_grid)

# min_max = [[-1,1], [-1,1], [-1,1]]


# #new_state = check_adjacents(dict_grid, min_max)

# xy = [[-1,1], [-1,1]]
# zs = [-1, 1]



# #for i in range(0, len(coordinates)):
#     #print(coordinates[i], states[i])

# #for i in range(0, 1):

# new_coordinates = []
# new_states = []

# #https://raw.githubusercontent.com/Greblys/adventOfCode2020/main/Day%2017%20-%20Conway%20Cubes/part1.txt

# for x in range(min_max[0][0], min_max[0][1]+1):
#     for y in range(min_max[1][0], min_max[1][1]+1):
#         for z in range(min_max[2][0], min_max[2][1]+1):
#             coordinate = [x, y, z]
#             new_state = check_adjacents(coordinate, coordinates, states)
#             new_coordinates.append(coordinate)
#             new_states.append(new_state)

# for i in range(0, len(new_states)):
#     if new_states[i] == 1:
#         print(new_coordinates[i])



