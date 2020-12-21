from collections import defaultdict

data = open('inputs/10.in').read().splitlines()
# data = open('inputs/10-example.in').read().splitlines()
# data = open('inputs/10-example2.in').read().splitlines()


def p1():
    nums = sorted(map(int, data))

    # these start at 1 since the results I was having were always 1 smaller
    # god knows why, but duct tape code for quick solutions since this is AoC! :D
    jump_1 = 1
    jump_3 = 1

    jolts = iter(nums)
    # Smallest one to start
    last_jolts = next(jolts)

    for curr_jolts in jolts:
        diff = curr_jolts - last_jolts
        if diff == 1:
            jump_1 += 1
        elif diff == 3:
            jump_3 += 1

        last_jolts = curr_jolts

    print(jump_1, jump_3)
    print(jump_1 * jump_3)


def p2():
    nums = set(map(int, data))

    # Start at the output capacity
    curr_jolt = max(nums) + 3

    paths = defaultdict(int)
    paths[curr_jolt] = 1

    while curr_jolt >= 0:
        if curr_jolt in nums or curr_jolt == 0:
            paths[curr_jolt] = paths[curr_jolt + 1] + paths[curr_jolt + 2] + paths[curr_jolt + 3]

        curr_jolt -= 1

    # print(paths)
    print("Sol:", paths[0])

p1()
p2()
