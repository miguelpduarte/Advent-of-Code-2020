import re

data = open('inputs/4.in').read().splitlines()
# data = open('inputs/4-example.in').read().splitlines()
# data = open('inputs/4-example2.in').read().splitlines()

parse_regex = re.compile(r'(\w+):([#\w]+)')

def line_to_kv(line):
    return parse_regex.findall(line)

# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID) (optional)

# , 'cid'
required_fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

def p1():
    found_fields = []
    n_valid = 0

    for line in data:
        # print(line)
        if line == '':
            # print(found_fields)
            if required_fields.intersection(found_fields) == required_fields:
                n_valid += 1
            found_fields = []
        else:
            for key, _value in line_to_kv(line):
                found_fields.append(key)
    # No newline at the end...
    if required_fields.intersection(found_fields) == required_fields:
        n_valid += 1

    print(n_valid)

def validate_p2(fields):
    if required_fields.intersection(fields.keys()) != required_fields:
        return False

    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    byr = int(fields['byr'])
    if byr < 1920 or byr > 2002:
        # print('byr')
        return False

    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    iyr = int(fields['iyr'])
    if iyr < 2010 or iyr > 2020:
        # print('iyr')
        return False

    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    eyr = int(fields['eyr'])
    if eyr < 2020 or eyr > 2030:
        # print('eyr')
        return False

    # hgt (Height) - a number followed by either cm or in:
    #     If cm, the number must be at least 150 and at most 193.
    #     If in, the number must be at least 59 and at most 76.
    hgt_val_raw, hgt_type = re.findall(r'(\d+)(\w+)', fields['hgt'])[0]
    hgt_val = int(hgt_val_raw)
    if hgt_type == 'cm':
        if hgt_val < 150 or hgt_val > 193:
            # print('hgt cm')
            return False
    elif hgt_type == 'in':
        if hgt_val < 59 or hgt_val > 76:
            # print('hgt in')
            return False
    else:
        # print('hgt oth')
        return False

    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    if not re.match(r'#[0-9a-f]{6}', fields['hcl']):
        # print('hcl')
        return False
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    if not fields['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        # print('ecl')
        return False
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    if not re.match(r'\d{9}', fields['pid']):
        # print('pid')
        return False
    # cid (Country ID) - ignored, missing or not.

    return True

def p2():
    found_fields = {}
    n_valid = 0

    for line in data:
        # print(line)
        if line == '':
            # print(found_fields)
            if validate_p2(found_fields):
                n_valid += 1
            found_fields = {}
        else:
            found_fields.update(line_to_kv(line))

    # No newline at the end...
    if validate_p2(found_fields):
        n_valid += 1

    print(n_valid)

p1()
p2()

# Note: p2 is 1 too high for some reason. Couldn't exactly find out why
