arq = open('input12.txt', 'r')

def rotate_ship(direction, num):
    global current_direction

    rotate = num//90

    if direction == "L":
        rotate = directions[current_direction] - rotate
    else:
        rotate = rotate + directions[current_direction]

    #print(rotate)
    if rotate <0:
        rotate = rotate + 4
    elif rotate > 3:
        rotate = rotate - 4

    current_direction = list(directions.keys())[rotate]

def move_ship(direction, num, north, east):
    if direction in ["N", "S"]:
        if direction == "N":
            north = north + num
        else:
            north = north - num
    else:
        if direction == "E":
            east = east + num
        else:
            east = east - num

    return(north, east)

def instructions_ship(action, north, east):
    global current_direction
    direction = action[0]
    num = int(action[1:])

    if direction in rotation:
        rotate_ship(direction, num)
    
    elif direction in directions:
        north, east = move_ship(direction, num, north, east)

    else:
        north, east = move_ship(current_direction, num, north, east)

    return(north, east)

#part2
def move_ship_waypoint(num, north, east, north_waypoint, east_waypoint):
    north = north + north_waypoint*num
    east = east + east_waypoint*num

    return(north, east)

def rotate_waypoint(direction, num, north_waypoint, east_waypoint):
    rotate = num//90

    if direction == "L":
        rotate = 4 - rotate

    if rotate == 1:
        new_north_waypoint = - east_waypoint
        new_east_waypoint = north_waypoint
    elif rotate == 2:
        new_north_waypoint = - north_waypoint
        new_east_waypoint = - east_waypoint
    elif rotate == 3:
        new_north_waypoint = east_waypoint
        new_east_waypoint = - north_waypoint
    else:
        new_north_waypoint = north_waypoint
        new_east_waypoint = east_waypoint
    
    return(new_north_waypoint, new_east_waypoint)
        

def instructions_waypoint(action, north, east, north_waypoint, east_waypoint):
    direction = action[0]
    num = int(action[1:])

    if direction in rotation:
        north_waypoint, east_waypoint = rotate_waypoint(direction, num, north_waypoint, east_waypoint)
    
    elif direction in directions:
        north_waypoint, east_waypoint = move_ship(direction, num, north_waypoint, east_waypoint)

    else:
        north, east = move_ship_waypoint(num, north, east, north_waypoint, east_waypoint)

    return(north, east, north_waypoint, east_waypoint)


directions = {"N":0, "E":1, "S":2, "W":3}
current_direction = "E"
rotation = ["L", "R"]
north = 0
east = 0
north_waypoint = 1
east_waypoint = 10


for line in arq:
    action = line.split()[0]
    #part1
    #north, east = instructions_ship(action, north, east)

    #part2
    north, east, north_waypoint, east_waypoint = instructions_waypoint(action, north, east, north_waypoint, east_waypoint)
    

print(abs(north)+abs(east))