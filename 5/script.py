def read_input():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    
    lines = [line.strip() for line in lines]

    return lines


def get_binary_search_result(input, min_range, max_range, upper_code, lower_code):

    lower = min_range
    upper = max_range

    for letter in input:
        if letter == upper_code:
            lower = (lower + upper) // 2 + 1
        elif letter == lower_code:
            upper = (lower + upper) // 2
        else:
            raise Exception("wrong code in boarding pass {}".format(letter))


    if upper != lower:
        raise Exception("Upper and lower don't match {} {}". format(lower, upper))

    return upper

def parse_pass(boarding_pass):
    row_part = boarding_pass[:7]
    column_part = boarding_pass[7:]
    
    row_num = get_binary_search_result(
        input=row_part,
        min_range=0,
        max_range=127,
        upper_code='B',
        lower_code='F'
    )

    column_num = get_binary_search_result(
        input=column_part,
        min_range=0,
        max_range=7,
        upper_code='R',
        lower_code='L'
    )

    seat_id = row_num * 8 + column_num

    return seat_id


def main():
    lines = read_input()

    seat_ids = [parse_pass(line) for line in lines]
    
    print("Max seat id: {}".format(max(seat_ids)))

    for seat_id in range(min(seat_ids), max(seat_ids) + 1):
        if seat_id not in seat_ids:
            print("My seat id is {}".format(seat_id))
            break


if __name__ == "__main__":
    main()