entries = [int(x) for x in open('inputs/1.in').read().splitlines()]


def part1():
    for idx_x, x in enumerate(entries):
        for idx_y, y in enumerate(entries):
            if idx_x == idx_y:
                continue

            if x + y == 2020:
                print(x*y)
                return
        
def part2():
    for x in entries:
        for y in entries:
            for z in entries:
                if x + y + z == 2020:
                    print(x*y*z)
                    return

# part1()
# part2()
