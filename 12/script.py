def read_input():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    
    lines = [line.strip() for line in lines]

    return lines


def move_ship(ship, direction, value):
    if direction == 'N':
        ship['N'] += value
    elif direction == 'S':
        ship['N'] -= value
    elif direction == 'E':
        ship['E'] += value
    elif direction == 'W':
        ship['E'] -= value


def main():
    lines = read_input()

    # part 1 position tracker
    position = {
        "N": 0,
        "E": 0,
        'direction': 0
    }

    # part 2 position trackers
    ship_position_part2 = {
        "N": 0,
        "E": 0
    }

    waypoint_relative_position_part2 = {
        "N": 1,
        "E": 10
    }

    directions = ['E', 'S', 'W', 'N']

    for line in lines:
        instruction = line[0]
        value = int(line[1:])

        if instruction in ['N', 'S', 'E', 'W']:
            move_ship(position, instruction, value)
            move_ship(waypoint_relative_position_part2, instruction, value)
        elif instruction == 'R':
            position['direction'] = (position['direction'] + (value / 90)) % 4 
            for i in range((value / 90)):
                temp = waypoint_relative_position_part2['E']
                waypoint_relative_position_part2['E'] = waypoint_relative_position_part2['N']
                waypoint_relative_position_part2['N'] = -temp
        elif instruction == 'L':
            position['direction'] = (position['direction'] - (value / 90)) % 4 
            for i in range((value / 90)):
                temp = waypoint_relative_position_part2['N']
                waypoint_relative_position_part2['N'] = waypoint_relative_position_part2['E']
                waypoint_relative_position_part2['E'] = -temp
        elif instruction == 'F':
            ship_position_part2['N'] += waypoint_relative_position_part2['N'] * value
            ship_position_part2['E'] += waypoint_relative_position_part2['E'] * value

            move_ship(position, directions[position['direction']], value)

    print(position)
    print(abs(position['N']) + abs(position['E']))

    print(ship_position_part2)
    print(abs(ship_position_part2['N']) + abs(ship_position_part2['E']))

        

if __name__ == "__main__":
    main()