def read_input():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    
    lines = [line.strip() for line in lines]

    return lines


def main():
    lines = read_input()

    game_nums = [int(num) for num in lines[0].split(',')]

    history = {}

    for idx, num in enumerate(game_nums[:-1]):
        history[num] = idx

    # TARGET_NUM = 2020
    TARGET_NUM = 30000000

    while len(game_nums) < TARGET_NUM:
        last_num = game_nums[-1]
        last_idx = len(game_nums) - 1

        if last_num not in history:
            game_nums.append(0)
        else:
            diff = last_idx - history[last_num]
            game_nums.append(diff)
        
        history[last_num] = last_idx

    print(game_nums[-1])

if __name__ == "__main__":
    main()