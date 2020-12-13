# data = open('inputs/12-example.in').read().splitlines()
data = open('inputs/12.in').read().splitlines()

#  N
# W E
#  S



# i miss pattern matching :(
def rotate_one(orientation, direction):
    if direction == 'L':
        if orientation == (1,0):
            return (0, -1)
        elif orientation == (0, -1):
            return (-1, 0)
        elif orientation == (-1, 0):
            return (0, 1)
        elif orientation == (0, 1):
            return (1, 0)
    elif direction == 'R':
        if orientation == (1,0):
            return (0, 1)
        elif orientation == (0, -1):
            return (1, 0)
        elif orientation == (-1, 0):
            return (0, -1)
        elif orientation == (0, 1):
            return (-1, 0)

def update_orientation(orientation, direction, angle):
    n_rotates = angle // 90
    for _ in range(n_rotates):
        orientation = rotate_one(orientation, direction)
    return orientation

def update_pos(coords, orientation, movetype, amount):
    if movetype == 'N':
        basevector = (0, -1)
    elif movetype == 'E':
        basevector = (1, 0)
    elif movetype == 'S':
        basevector = (0, 1)
    elif movetype == 'W':
        basevector = (-1, 0)
    elif movetype == 'F':
        basevector = orientation

    scaled_vector = tuple(amount*x for x in basevector)
    return tuple(coord1 + coord2 for coord1, coord2 in zip(coords, scaled_vector))

# init is east
orientation = (1, 0)
# considering the top left corner to be 0,0, south and east are positive
coords = (0, 0)

for line in data:
    movement_type = line[0]
    amount = int(line[1:])
    if movement_type == 'L' or movement_type == 'R':
        orientation = update_orientation(orientation, movement_type, amount)
    else:
        coords = update_pos(coords, orientation, movement_type, amount)
    # print(f"{coords} - {orientation}")

print(coords)
print(sum(tuple(abs(x) for x in coords)))
