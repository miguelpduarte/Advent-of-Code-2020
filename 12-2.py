from math import cos, sin, radians

# data = open('inputs/12-example.in').read().splitlines()
data = open('inputs/12.in').read().splitlines()

def rotate_around_origin(coords, direction, angle):
    if direction == 'R':
        multiplier = 1
    else:
        multiplier = -1

    angle_rads = radians(multiplier * angle)

    old_x, old_y = coords
    x = round(old_x*cos(angle_rads) - old_y*sin(angle_rads))
    y = round(old_y*cos(angle_rads) + old_x*sin(angle_rads))

    return (x, y)

def update_pos(coords, movetype, amount):
    if movetype == 'N':
        basevector = (0, -1)
    elif movetype == 'E':
        basevector = (1, 0)
    elif movetype == 'S':
        basevector = (0, 1)
    elif movetype == 'W':
        basevector = (-1, 0)

    scaled_vector = tuple(amount*x for x in basevector)
    return tuple(coord1 + coord2 for coord1, coord2 in zip(coords, scaled_vector))

def move_to_waypoint(ship_coords, waypoint, amount):
    # move towards the waypoint 'amount' times
    scaled_waypoint_movement = tuple(amount*x for x in waypoint)
    return tuple(coord1 + coord2 for coord1, coord2 in zip(ship_coords, scaled_waypoint_movement))

# considering the top left corner to be 0,0, south and east are positive
ship_coords = (0, 0)
# relative coordinates
waypoint = (10, -1)

for line in data:
    movement_type = line[0]
    amount = int(line[1:])
    if movement_type == 'L' or movement_type == 'R':
        waypoint = rotate_around_origin(waypoint, movement_type, amount)
    elif movement_type == 'F':
        ship_coords = move_to_waypoint(ship_coords, waypoint, amount)
    else:
        # Just moves the waypoint now
        waypoint = update_pos(waypoint, movement_type, amount)
    # print(f"{ship_coords} - {waypoint}")

print(ship_coords)
print(waypoint)
print(sum(tuple(abs(x) for x in ship_coords)))
