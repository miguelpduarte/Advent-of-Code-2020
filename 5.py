data = open('inputs/5.in').read().splitlines()
# data = open('inputs/5-example.in').read().splitlines()

def get_seat_pos(coords):
    row_data = coords[:-3]
    col_data = coords[-3:]

    row_min = 0
    row_max = 127
    for row_char in row_data:
        if row_char == 'F':
            row_max = row_min + (row_max - row_min) // 2
        elif row_char == 'B':
            row_min = row_min + (row_max - row_min) // 2 + 1

    assert row_min == row_max

    col_min = 0
    col_max = 7
    for col_char in col_data:
        if col_char == 'L':
            col_max = col_min + (col_max - col_min) // 2
        elif col_char == 'R':
            col_min = col_min + (col_max - col_min) // 2 + 1

    return (row_min, col_min)

def coords_to_seat_id(coords):
    row, col = coords
    return row * 8 + col

def p1():
    max_seat_id = 0

    for line in data:
        seat = get_seat_pos(line)
        # print(seat)
        seat_id = coords_to_seat_id(seat)
        max_seat_id = max(seat_id, max_seat_id)

    print(max_seat_id)

def p2():
    seat_ids = []

    for line in data:
        seat = get_seat_pos(line)
        # print(seat)
        seat_id = coords_to_seat_id(seat)
        seat_ids.append(seat_id)
    
    # print(sorted(seat_ids))
    last_elem = None
    for seat_id in sorted(seat_ids):
        if last_elem and seat_id > last_elem + 1:
            print(seat_id - 1)
            return

        last_elem = seat_id

p2()
