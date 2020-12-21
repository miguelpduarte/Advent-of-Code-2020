data = open('inputs/9.in').read().splitlines()
# data = open('inputs/9-example.in').read().splitlines()

def is_valid(preamble, num):
    for x in preamble:
        if (num - x) in preamble:
            return True
    return False

def p1():
    # preamble = set(map(int, data[:25]))
    # print(preamble)
    nums = list(map(int, data))

    start_idx = 25

    for i in range(start_idx, len(nums)):
        num = nums[i]
        # look at last 5/25 or less depending on the idx
        # before = nums[max(i-5, 0):i]
        before = nums[max(i-25, 0):i]

        if not is_valid(before, num):
            print(num)
            return num
def p2(invalid_num):
    nums = list(map(int, data))

    # the set of contiguous number must be of at least two
    left_idx = 0
    right_idx = 2

    while True:
        sum_so_far = sum(nums[left_idx:right_idx])

        if sum_so_far == invalid_num:
            min_num = min(nums[left_idx:right_idx])
            max_num = max(nums[left_idx:right_idx])
            print(min_num+max_num)
            return

        if sum_so_far > invalid_num:
            # We are over the target value, move the left index up
            left_idx += 1
        else:
            # Otherwise just keep on increasing the right index, increasing the window
            right_idx += 1

invalid_num = p1()
p2(invalid_num)
