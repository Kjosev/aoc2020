def read_input():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    return lines


def get_res(map, dx, dy):
    columns = len(map[0].strip())
    rows = len(map)
    count_trees = 0
    # print("dx {} dy {}".format(dx, dy))
    for i, row in enumerate(map):
        if i == 0 or i % dy != 0:
            continue
        
        idx_to_check = ((i / dy) * dx) % columns
        # print("i {} idx {}".format(i, idx_to_check))
        if row[idx_to_check] == '#':
            count_trees += 1
    print(count_trees)
    return count_trees


def main():
    map = read_input()

    dx = 3
    dy = 1

    result = 1

    for (dx, dy) in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        result *= get_res(map, dx, dy)

    print(result)


if __name__ == "__main__":
    main()