def read_input():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    
    lines = [line.strip() for line in lines]

    return lines


def run_program(lines, op_to_switch=None):
    visited = set()
    accumulator = 0
    current_idx = 0

    finished_normally = False
    while current_idx not in visited:
        if current_idx >= len(lines):
            finished_normally = True
            break

        (op, num) = lines[current_idx]
        num = int(num)

        if op_to_switch == current_idx:
            op = 'jmp' if op == 'nop' else 'nop'

        if op == 'nop':
            next_idx = current_idx + 1
        elif op == 'acc':
            accumulator += num
            next_idx = current_idx + 1
        elif op == 'jmp':
            next_idx = current_idx + num

        visited.add(current_idx)
        current_idx = next_idx

    return {
        "result": accumulator,
        "finished_normally": finished_normally
    }


def find_and_fix_wrong_op(lines):
    for idx, (op, num) in enumerate(lines):
        if op == 'nop' or op == 'jmp':
            output = run_program(lines, op_to_switch=idx)
            if output["finished_normally"]:
                return output["result"]



def main():
    lines = read_input()
    parsed_lines = [line.split() for line in lines]

    result_1 = run_program(parsed_lines)
    print(result_1)

    result_2 = find_and_fix_wrong_op(parsed_lines)
    print(result_2)

if __name__ == "__main__":
    main()