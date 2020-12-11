from operator import mul
from functools import reduce

# map = open('inputs/3-example.in').read().splitlines()
map = open('inputs/3.in').read().splitlines()

def p1():
    tree_count = 0

    for y in range(len(map)):
        x_idx = (y*3) % len(map[y])

        if map[y][x_idx] == '#':
            tree_count += 1

    print(tree_count)

def p2():
    tree_counts = [0]*5

    for y in range(len(map)):
        # Right 1, down 1.
        if map[y][y % len(map[y])] == '#':
            tree_counts[0] += 1
        # Right 3, down 1. (This is the slope you already checked.)
        if map[y][(y*3) % len(map[y])] == '#':
            tree_counts[1] += 1
        # Right 5, down 1.
        if map[y][(y*5) % len(map[y])] == '#':
            tree_counts[2] += 1
        # Right 7, down 1.
        if map[y][(y*7) % len(map[y])] == '#':
            tree_counts[3] += 1
        # Right 1, down 2.
        if y % 2 == 0 and map[y][(y//2) % len(map[y])] == '#':
            tree_counts[4] += 1

    print(tree_counts)
    print(reduce(mul, tree_counts, 1))

p1()
p2()
