def read_input():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    
    lines = [line.strip() for line in lines]

    return lines


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def ChineseRemainderGauss(n, a):
    result = 0

    N = 1
    for ni in n: 
        N *= ni

    for i in range(len(n)):
        ai = a[i]
        ni = n[i]
        bi = N // ni

        result += ai * bi * modinv(bi, ni)

    return N - result % N


def part2():
    lines = read_input()
    busses_w_idxs = [(int(bus), idx) for idx, bus in enumerate(lines[1].split(',')) if bus != 'x']

    print(ChineseRemainderGauss(n=[bus[0] for bus in busses_w_idxs], a=[bus[1] for bus in busses_w_idxs]))


def part1():
    lines = read_input()

    earliest_timestamp = int(lines[0])

    busses = [int(bus) for bus in lines[1].split(',') if bus != 'x']

    earliest_acceptable_bus_departure = 999999999999999999999
    bus_to_take = -1

    for bus_cadance in busses:

        if earliest_timestamp % bus_cadance == 0:
            earliest_acceptable_bus_departure = earliest_timestamp
            break

        num_trips_before_acceptable = (earliest_timestamp // bus_cadance)

        current_earliest_acceptable_bus_departure = (num_trips_before_acceptable + 1) * bus_cadance

        if current_earliest_acceptable_bus_departure < earliest_acceptable_bus_departure:
            earliest_acceptable_bus_departure = current_earliest_acceptable_bus_departure
            bus_to_take = bus_cadance

    minutes_to_wait = earliest_acceptable_bus_departure - earliest_timestamp
    print(bus_to_take * minutes_to_wait)

if __name__ == "__main__":
    part1()
    part2()