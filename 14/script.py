import re

def read_input():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    
    lines = [line.strip() for line in lines]

    return lines


def derive_value(value, mask):
    zero_mask = ['0' if letter == '0' else '1' for letter in mask]
    one_mask = ['1' if letter == '1' else '0' for letter in mask]

    zero_mask = int(''.join(zero_mask), 2) 
    one_mask = int(''.join(one_mask), 2)

    # apply 1s
    value = value | one_mask
    # apply 0s
    value = value & zero_mask

    return value


def generate_all_possible_masks(mask):
    if len(mask) == 0:
        return ['']

    suffix_masks = generate_all_possible_masks(mask[1:])
    if mask[0] == '0':
        return ['X' + suffix_mask for suffix_mask in suffix_masks]
    elif mask[0] == '1':
        return ['1' + suffix_mask for suffix_mask in suffix_masks]
    elif mask[0] == 'X':
        zero_masks = ['0' + suffix_mask for suffix_mask in suffix_masks]
        one_masks = ['1' + suffix_mask for suffix_mask in suffix_masks]
        return zero_masks + one_masks


def derive_addresses(value, masks):
    values = set()
    for mask in masks:
        values.add(derive_value(value, mask))
    return values


def main():
    
    lines = read_input()

    mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    masks = [mask]

    mem = {}
    mem2 = {}

    for line in lines:
        if line[:4] == 'mask':
            m = re.match(r'mask = ([X01]+)', line)
            mask = m.groups()[0]
            masks = generate_all_possible_masks(mask)
        else:
            m = re.match(r'mem\[(\d+)\] = (\d+)', line)
            matched = m.groups()
            idx = int(matched[0])
            value = int(matched[1])

            mem[idx] = derive_value(value, mask)

            for address in derive_addresses(idx, masks):
                mem2[address] = value
    

    print(sum(mem.values()))
    print(sum(mem2.values()))

if __name__ == "__main__":
    main()