import re

parse_regex = re.compile(r'(\d+)-(\d+) (\w): (\w+)')

def parse_line(line):
    return parse_regex.findall(line)[0]

data = [parse_line(x) for x in open('inputs/2.in').read().splitlines()]

valid = 0
valid_p2 = 0

for (min_count, max_count, char, pw) in data:
    char_count = pw.count(char)
    if char_count >= int(min_count) and char_count <= int(max_count):
        valid += 1 

    if (pw[int(min_count)-1] == char) ^ (pw[int(max_count)-1] == char):
        valid_p2 += 1

print(valid)
print(valid_p2)
