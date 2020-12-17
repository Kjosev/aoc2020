def read_input():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    
    lines = [line.strip() for line in lines]

    return lines


def init_grid(lines, padding):
    grid = {}

    num_rows = len(lines)
    num_columns = len(lines[0])

    ACTIVE = '#'
    INACTIVE = '.'

    for row in range(-padding, num_rows + padding + 1):
        for column in range(- padding, num_columns + padding + 1):
            for depth in range(-padding, padding + 1):
                grid[(row, column, depth)] = {
                    "active": False,
                    "count_adjacenet_active": 0
                }

    for row_idx, line in enumerate(lines):
        for col_idx, char in enumerate(line):
            if char == ACTIVE:
                grid[(row_idx, col_idx, 0)]['active'] = True

    return grid


def run_cycle(grid):
    grid = count_adjacent_active(grid)
    grid = flip_active(grid)
    return grid


def count_adjacent_active(grid):
    for (curr_row, curr_col, curr_depth), cube in grid.items():
        adjecent_cubes = get_adjecent_cubes(grid, curr_row, curr_col, curr_depth)
        active_count = count_active(adjecent_cubes)
        cube['count_adjacenet_active'] = active_count

    return grid


def count_active(cubes):
    return sum([1 for cube in cubes if cube['active'] == True])
                    

def get_adjecent_cubes(grid, curr_row, curr_col, curr_depth):
    adjecent_cubes = []
    for row in range(curr_row - 1, curr_row + 2 ):
        for col in range(curr_col - 1, curr_col + 2 ):
            for depth in range(curr_depth - 1, curr_depth + 2 ):
                if row == curr_row and col == curr_col and depth == curr_depth:
                    continue
                adjecent_cubes.append(grid.get((row, col, depth), None))

    return [cube for cube in adjecent_cubes if cube is not None] 


def flip_active(grid):
    for cube in grid.values():
        if cube['active'] == True and cube['count_adjacenet_active'] not in [2, 3]:
            cube['active'] = False
        elif cube['active'] == False and cube['count_adjacenet_active'] == 3:
            cube['active'] = True

    return grid


def print_grid(grid):

    all_rows = sorted(set([key[0] for key in grid.keys()]))
    all_cols = sorted(set([key[1] for key in grid.keys()]))
    all_depths = sorted(set([key[2] for key in grid.keys()]))

    for depth in all_depths:
        print("Depth: {}".format(depth))

        for row in all_rows:
            row_str = ""
            for col in all_cols:
                row_str += '#' if grid[(row, col, depth)]['active'] else '.'
            print(row_str)

def main():
    NUM_CYCLES = 6

    lines = read_input()
    grid = init_grid(lines, padding=NUM_CYCLES)

    # print_grid(grid)

    for i in range(NUM_CYCLES):
        grid = run_cycle(grid)

        # print("Cycle {}".format(i + 1))
        # print_grid(grid)

    print(count_active(grid.values()))


if __name__ == "__main__":
    main()