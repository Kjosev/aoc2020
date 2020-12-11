def read_input():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    
    lines = [line.strip() for line in lines]

    return lines


FREE_SEAT = 'L'
TAKEN_SEAT = '#'
FLOOR = '.'

CROWDED_THRESHOLD = 5
# CROWDED_THRESHOLD = 4


def get_occupied_seats_count(grid, col, row, strategy='PART1', adjecent_seat_precomputed=None):
    num_cols = len(grid)
    num_rows = len(grid[0])

    count_occupied = 0

    if strategy == 'PART1':
        adjecent_seat_idx = [
            (col - 1, row - 1),
            (col - 1, row),
            (col - 1, row + 1),
            (col, row - 1),
            (col, row + 1),
            (col + 1, row - 1),
            (col + 1, row),
            (col + 1, row + 1),
        ]
    else:
        adjecent_seat_idx = adjecent_seat_precomputed[col][row]


    for col_to_check, row_to_check in adjecent_seat_idx:
        col_in_bounds = col_to_check >= 0 and col_to_check < num_cols
        row_in_bounds = row_to_check >= 0 and row_to_check < num_rows

        if col_in_bounds and row_in_bounds:
            count_occupied += 1 if grid[col_to_check][row_to_check] == TAKEN_SEAT else 0

    return count_occupied


def find_first_seat(grid, col, row, d_col, d_row):
    num_cols = len(grid)
    num_rows = len(grid[0])
    
    col_to_check = col + d_col
    row_to_check = row + d_row

    col_in_bounds = col_to_check >= 0 and col_to_check < num_cols
    row_in_bounds = row_to_check >= 0 and row_to_check < num_rows

    while col_in_bounds and row_in_bounds:
        is_seat = grid[col_to_check][row_to_check] == FREE_SEAT or grid[col_to_check][row_to_check] == TAKEN_SEAT

        if is_seat:
            return (col_to_check, row_to_check)
        
        col_to_check += d_col
        row_to_check += d_row
        col_in_bounds = col_to_check >= 0 and col_to_check < num_cols
        row_in_bounds = row_to_check >= 0 and row_to_check < num_rows

    return None


def precompute_adjecent_seats(grid):

    adjecent_seat_precomputed = [[[] for seat in line] for line in grid]
    
    num_cols = len(grid)
    num_rows = len(grid[0])

    for col in range(num_cols):
        for row in range(num_rows):
            d_col = [-1, -1, -1, 0, 0, 1, 1, 1]
            d_row = [-1, 0, 1, -1, 1, -1, 0, 1]

            for idx in range(len(d_col)):
                first_seat = find_first_seat(grid, col, row, d_col[idx], d_row[idx])
                if first_seat:
                    adjecent_seat_precomputed[col][row].append(first_seat)

    return adjecent_seat_precomputed


def main():
    grid = read_input()

    grid = [list(line) for line in grid]

    num_cols = len(grid)
    num_rows = len(grid[0])


    adjecent_seat_precomputed = precompute_adjecent_seats(grid)
    
    changed = True
    while changed:
        changed = False
        count_occupied = [[0 for y in grid[0]]for x in grid]

        for col in range(num_cols):
            for row in range(num_rows):
                # count_occupied[col][row] = get_occupied_seats_count(grid, col, row, strategy='PART1')
                count_occupied[col][row] = get_occupied_seats_count(
                    grid, col, row, strategy='PART2', adjecent_seat_precomputed=adjecent_seat_precomputed)
        

        for col in range(num_cols):
            for row in range(num_rows):
                is_seat_occupied = grid[col][row] == TAKEN_SEAT
                is_seat_free = grid[col][row] == FREE_SEAT

                if is_seat_occupied and count_occupied[col][row] >= CROWDED_THRESHOLD:
                    grid[col][row] = FREE_SEAT
                    changed = True
                elif is_seat_free and count_occupied[col][row] == 0:
                    grid[col][row] = TAKEN_SEAT
                    changed = True


    occupied_seat_count = sum([sum([1 for seat in row if seat == TAKEN_SEAT]) for row in grid])
    print(occupied_seat_count)


if __name__ == "__main__":
    main()