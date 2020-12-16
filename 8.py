data = open('inputs/8.in').read().splitlines()
# data = open('inputs/8-example.in').read().splitlines()

def run_fasm(changed_idx = None):
    idx = 0
    ecx = 0
    instructions_seen = set()
    n_insts = len(data)

    while True:
        if idx >= n_insts:
            break
        line = data[idx]
        opcode = line[:3]
        # print(idx)

        if idx in instructions_seen:
            return {'ended': False, 'ecx': ecx, 'idx': idx}

        instructions_seen.add(idx)

        if opcode == 'nop' or (changed_idx == idx and opcode == 'jmp'):
            idx += 1
            continue

        num = int(line[3:])

        if opcode == 'acc':
            idx += 1
            ecx += num
            continue

        if opcode == 'jmp' or (changed_idx == idx and opcode == 'nop'):
            idx += num
        else:
            print('uh oh')
            raise Exception()
    return {'ended': True, 'ecx': ecx, 'idx': idx}

def p1():
    res = run_fasm()
    print(f"#{res['idx']} repeated, ecx={res['ecx']}")

def p2():
    for i in range(len(data)):
        opcode = data[i][:3]
        if opcode == 'nop':
            continue
        res = run_fasm(i)
        if res['ended']:
            print(f"Finished! Swapped {i}, ecx={res['ecx']}")
            break

p1()
p2()
