data = open('inputs/6.in').read().splitlines()
# data = open('inputs/6-example.in').read().splitlines()

def p1():
    ans_count = 0
    group_answers = set()

    for line in data:
        if line == '':
            # Group end
            ans_count += len(group_answers)
            group_answers = set()
        else:
            group_answers.update(list(line))

    # No newline in end
    ans_count += len(group_answers)

    print(ans_count)

def p2():
    ans_count = 0
    group_answers = set()
    group_start = True

    for line in data:
        if line == '':
            # Group end
            # print(group_answers)
            # print(len(group_answers))
            ans_count += len(group_answers)
            group_answers = set()
            group_start = True
        else:
            if group_start:
                # Start of group, take all and start intersecting later
                group_answers.update(list(line))
                group_start = False
            else:
                # Intersect to get common
                group_answers = group_answers.intersection(list(line))

    # No newline in end
    ans_count += len(group_answers)

    print(ans_count)

p1()
p2()
