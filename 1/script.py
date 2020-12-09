def read_input():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    return lines


def main():
    input = read_input()
    parsed = [int(line) for line in input]

    # part 1
    for i, val1 in enumerate(parsed):
        for j, val2 in enumerate(parsed):
            if j >= i:
                continue
        
            if val1 + val2 == 2020:
                print("PART 1: {} * {} = {}".format(val1, val2, val1 * val2))
    
    # part 2
    for i, val1 in enumerate(parsed):
        for j, val2 in enumerate(parsed):
            for k, val3 in enumerate(parsed):
                if j >= i or k >= j:
                    continue
        
                if val1 + val2 + val3 == 2020:
                    print("PART 2{} * {} * {} = {}".format(val1, val2, val3, val1 * val2 * val3))

        


if __name__ == "__main__":
    main()